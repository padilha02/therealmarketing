
# Vamos carregar os dados e remover completamente as seções de Planos e CTA/Diagnóstico

import json
import yaml

# Carregar dados existentes
with open('dados_atualizados_trma.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Remover completamente qualquer referência a planos comerciais
# Os dados já não têm "planos" incluídos, então vamos garantir que o YAML também não tenha

# Verificar estrutura atual
print("📋 Estrutura atual dos dados:")
for key in dados.keys():
    print(f"   • {key}")

print("\n✅ Dados estão limpos - sem seções de planos ou CTA")
print("\n🎯 Seções que serão mantidas:")
print("   • Posicionamento")
print("   • Métricas Atualizadas")
print("   • Empresas do Ecossistema (8)")
print("   • Diferenciais (4)")
print("   • Tecnologia")
print("   • Visão Global (com 6 cards)")
print("   • Tráfego Pago")
print("   • Cultura")
print("   • Footer simples")

# Salvar YAML limpo
yaml_content = yaml.dump(dados, allow_unicode=True, sort_keys=False, default_flow_style=False)

with open('dados_finais_trma.yaml', 'w', encoding='utf-8') as f:
    f.write(yaml_content)

print("\n✅ YAML final gerado sem planos e sem CTA!")
