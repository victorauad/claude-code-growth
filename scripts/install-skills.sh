#!/bin/bash
# Instala as skills do co-coach em outro projeto.
# Uso: bash install-skills.sh /caminho/do/projeto
# Exemplo: bash install-skills.sh ~/meu-projeto-hubspot

set -e

SKILLS_SOURCE="$(cd "$(dirname "$0")/.." && pwd)/skills"
TARGET_PROJECT="${1:-}"

if [ -z "$TARGET_PROJECT" ]; then
  echo "Erro: informe o caminho do projeto alvo."
  echo "Uso: bash install-skills.sh /caminho/do/projeto"
  exit 1
fi

if [ ! -d "$TARGET_PROJECT" ]; then
  echo "Erro: pasta '$TARGET_PROJECT' não encontrada."
  exit 1
fi

TARGET_SKILLS="$TARGET_PROJECT/.claude/skills"
mkdir -p "$TARGET_SKILLS"

echo "Instalando skills em: $TARGET_SKILLS"
echo ""

for skill_dir in "$SKILLS_SOURCE"/*/; do
  skill_name=$(basename "$skill_dir")
  dest="$TARGET_SKILLS/$skill_name"

  if [ -d "$dest" ]; then
    echo "  ⚠️  $skill_name já existe — pulando (delete a pasta para reinstalar)"
  else
    cp -r "$skill_dir" "$dest"
    echo "  ✅ $skill_name instalada"
  fi
done

echo ""
echo "Pronto. Skills disponíveis no projeto '$TARGET_PROJECT':"
ls "$TARGET_SKILLS"
echo ""
echo "Para atualizar no futuro:"
echo "  1. git pull neste repo (co-coach)"
echo "  2. Delete as skills que quer atualizar em $TARGET_SKILLS"
echo "  3. Rode este script novamente"
