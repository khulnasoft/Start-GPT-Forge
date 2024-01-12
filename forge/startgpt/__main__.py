import os

from dotenv import load_dotenv

load_dotenv()
import startgpt.sdk.forge_log

startgpt.sdk.forge_log.setup_logger()


LOG = startgpt.sdk.forge_log.ForgeLogger(__name__)

if __name__ == "__main__":
    """Runs the agent server"""

    # modules are imported here so that logging is setup first
    import startgpt.agent
    import startgpt.sdk.db
    from startgpt.benchmark_integration import add_benchmark_routes
    from startgpt.sdk.workspace import LocalWorkspace

    router = add_benchmark_routes()

    database_name = os.getenv("DATABASE_STRING")
    workspace = LocalWorkspace(os.getenv("AGENT_WORKSPACE"))
    port = os.getenv("PORT")

    database = startgpt.sdk.db.AgentDB(database_name, debug_enabled=True)
    agent = startgpt.agent.StartGPTAgent(database=database, workspace=workspace)

    agent.start(port=port, router=router)
