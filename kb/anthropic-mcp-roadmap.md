---
titulo: "Roadmap do Model Context Protocol (MCP)"
tema: mcp
url: https://modelcontextprotocol.io/development/roadmap
data: 2026-06-22
fonte: anthropic-docs
importancia: alta
---

# Roadmap do MCP

Prioridades estratégicas do MCP para o ecossistema (atualizado março/2026).

## 1. Transport Evolution and Scalability

**Objetivo:** Streamable HTTP rodando em múltiplas instâncias, stateless, com session handling escalável.

- **Next-gen transport**: HTTP stateless em múltiplos servidores com suporte a load balancers
- **Scalable session handling**: sessões criadas, retomadas e migradas de forma transparente
- **MCP Server Cards**: padrão `.well-known` para descoberta de capacidades sem conexão

## 2. Agent Communication

Fechar lacunas do Tasks primitive (SEP-1686):
- **Retry semantics**: o que acontece com falhas transientes e quem decide se retentar
- **Expiry policies**: quanto tempo os resultados ficam disponíveis após conclusão

## 3. Governance Maturation

MCP agora é padrão multi-empresa sob Linux Foundation. Próximos passos:
- **Contributor Ladder** com progressão clara de papéis
- **Delegation model**: WGs com histórico comprovado podem aceitar SEPs no próprio domínio
- **Charter template** revisado trimestralmente por WG/IG

## 4. Enterprise Readiness

- **Audit trails e observabilidade**: rastreamento end-to-end para compliance
- **Enterprise-managed auth**: SSO-integrated flows para gestão de TI
- **Gateway e proxy patterns**: comportamento definido para intermediários
- **Configuration portability**: configurar servidor uma vez e funcionar em vários clientes MCP

## No Horizonte (prioridade futura)

- Triggers e Event-Driven Updates (webhooks para notificações proativas)
- Result Type Improvements (streaming, referências para payloads grandes)
- Security & Authorization (scopes granulares, credential management)
- Extensions Ecosystem (Skills primitive, marketplace de extensões)

## Como Participar

- [Grupos de Trabalho e Interesse](https://modelcontextprotocol.io/community/working-interest-groups)
- [SEP guidelines](https://modelcontextprotocol.io/community/sep-guidelines)
- [Contributing guide](https://modelcontextprotocol.io/community/contributing)
