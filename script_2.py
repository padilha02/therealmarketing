
# Ler YAML completo para enviar ao app_subagent
with open('dados_finais_trma.yaml', 'r', encoding='utf-8') as f:
    yaml_final = f.read()

print(yaml_final)
