"""Project configuration module."""

from pydantic import Field
from pydantic_settings import BaseSettings


class ProjectConfig(BaseSettings):
  """Project configuration settings."""

  TG_BOT_TOKEN = Field(..., description="Tg bot token for connection")
  LLM_API_KEY = Field(..., description="API key for connection with LLM")
  EXCEL_DIRECT_LINK = Field(..., description="Link to work with excel")

  class Config:
      """Pydantic configuration for environment variables."""

      env_file = ".env"
      env_file_encoding = "utf-8"
      case_sensitive = False
      extra = "allow"


project_config = ProjectConfig()
