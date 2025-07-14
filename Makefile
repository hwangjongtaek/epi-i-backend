# Makefile for Epi-i Backend

.PHONY: run lint format test migration-create migration-apply

# =============================================================================
# DEVELOPMENT
# =============================================================================

run:
	@echo "Starting development server..."
	@uvicorn app.main:app --reload

# =============================================================================
# CODE QUALITY
# =============================================================================

lint:
	@echo "Running linter..."
	@ruff check .

format:
	@echo "Formatting code..."
	@ruff format .


test:
	@echo "Running tests..."
	@pytest

# =============================================================================
# DATABASE MIGRATIONS (using Supabase CLI)
# =============================================================================

migration-create:
	@echo "Creating new database migration..."
	@# Example using Supabase CLI: supabase migration new <migration_name>
	@echo "Please replace the command above with your actual Supabase CLI command."


migration-apply:
	@echo "Applying database migrations..."
	@# Example using Supabase CLI: supabase db push
	@echo "Please replace the command above with your actual Supabase CLI command."

