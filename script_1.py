
# Recriar os dados limpos sem planos
import json
import yaml

dados_finais = {
    "posicionamento": {
        "nome": "The Real Marketing Agency",
        "slogan": "DO BRASIL PARA O MUNDO!",
        "tagline": "Somos o ecossistema que transforma dados em faturamento e promessas em lucro real",
        "descricao": "O primeiro ecossistema brasileiro de marketing, IA e automação",
        "origem": "Nascido dentro da Trip Angle, a maior comunidade de network digital do país"
    },
    
    "metricas_atualizadas": {
        "profissionais": "18.000+",
        "empresas": "100+",
        "faturamento_gerenciado": "R$ 60M+",
        "crescimento_medio": "470%",
        "roi_medio": "5x a 9x",
        "aumento_receita_b2b": "42%",
        "recorrencia_mensal": "26K",
        "faturamento_segmento": "12.5M"
    },
    
    "empresas_ecossistema": [
        {
            "id": 1,
            "nome": "Trip Angle",
            "descricao": "A maior comunidade de networking digital do Brasil, com mais de 15.000 membros ativos distribuídos em 9 grupos especializados, promovendo conexões e colaboração",
            "tipo": "Comunidade"
        },
        {
            "id": 2,
            "nome": "Escola de Prompt",
            "descricao": "Oferece ensino avançado em engenharia de prompts, capacitando inúmeros alunos com as habilidades essenciais para a era da inteligência artificial",
            "tipo": "Educação"
        },
        {
            "id": 3,
            "nome": "Navigator Brasil",
            "descricao": "Uma agência de alta performance que já atendeu mais de 40 empresas, entregando resultados e otimizando estratégias digitais",
            "tipo": "Agência"
        },
        {
            "id": 4,
            "nome": "AIM3",
            "descricao": "Especializada em transformação digital com IA, esta agência já serviu mais de 35 empresas e é a única do ecossistema com SaaS e atendimentos públicos no Rio de Janeiro",
            "tipo": "Agência"
        },
        {
            "id": 5,
            "nome": "LUNA AI",
            "descricao": "Uma solução SaaS de ponta que atua como assistente de IA avançada para empresas, otimizando processos e decisões",
            "tipo": "SaaS"
        },
        {
            "id": 6,
            "nome": "Marketing Sob Medida",
            "descricao": "Unidade vertical especializada no ramo moveleiro, com uma performance projetada para 2025 de R$ 11,2 milhões de faturamento gerenciado com apenas 6 empresas",
            "tipo": "Agência Vertical"
        },
        {
            "id": 7,
            "nome": "TragetX",
            "descricao": "Empresa de gestão de frotas integrada ao ecossistema, aplicando tecnologia para uma significativa redução de custos operacionais",
            "tipo": "Tecnologia"
        },
        {
            "id": 8,
            "nome": "Access Prime",
            "descricao": "A primeira bilheteria do mercado a operar com 0% de taxa, revolucionando a venda de ingressos e eventos",
            "tipo": "Fintech"
        }
    ],
    
    "diferenciais": [
        "Comunidade + Estratégia",
        "IA + Automação",
        "Tráfego + Conversão",
        "Branding + Dados"
    ],
    
    "tecnologia": {
        "luna_ai": "Assistente corporativa com automação total",
        "stack_automacoes": "n8n, conectando marketing, CRM e vendas",
        "dashboards": "Dashboards preditivos medindo cada clique, lead e ROI",
        "ia_generativa": "Copy, voz e vídeo em escala industrial"
    },
    
    "visao_global": {
        "plano": "2025-2027",
        "pilares": [
            {
                "numero": "01",
                "titulo": "Expansão Global",
                "descricao": "LATAM, Portugal e Estados Unidos"
            },
            {
                "numero": "02",
                "titulo": "Tecnologia Proprietária",
                "descricao": "IA brasileira de ponta e inovação nacional"
            },
            {
                "numero": "03",
                "titulo": "Compliance Internacional",
                "descricao": "LGPD, GDPR, CCPA - prontos para o mundo"
            },
            {
                "numero": "04",
                "titulo": "Certificações Premium",
                "descricao": "Google Partner Premier, Meta Business Partner, AWS"
            },
            {
                "numero": "05",
                "titulo": "ROI Comprovado",
                "descricao": "5x a 9x de retorno médio para nossos clientes"
            },
            {
                "numero": "06",
                "titulo": "Crescimento Exponencial",
                "descricao": "470% de crescimento médio em vendas online"
            }
        ],
        "tagline": "Brazilian Innovation in Digital Performance",
        "mensagem": "A criatividade é brasileira. A execução é mundial."
    },
    
    "trafego": {
        "meta_ads": {
            "titulo": "Alcance Massivo e Segmentação Precisa",
            "descricao": "Conecte-se com milhões de usuários no Facebook, Instagram e Audience Network, utilizando segmentação detalhada para atingir seu público ideal"
        },
        "google_ads": {
            "titulo": "Captura de Demanda e Visibilidade Global",
            "descricao": "Esteja presente no momento exato da intenção de compra, dominando a busca e a rede de display para atrair leads qualificados"
        },
        "estrategia_integrada": {
            "titulo": "Estratégia Integrada para Maximizar Resultados",
            "descricao": "Combinamos o poder da Meta e do Google para criar campanhas sinérgicas que amplificam sua presença, geram leads e escalam seu faturamento"
        }
    },
    
    "cultura": {
        "frase_impacto": "Não vendemos teoria. Fabricamos resultado em escala.",
        "mentalidade": "Uma só mentalidade: faturar todo santo dia",
        "promessa": "Esses números não são promessa, são padrão",
        "posicionamento": "A gente não reage ao mercado, a gente o antecipa"
    }
}

# Salvar JSON
with open('dados_finais_trma.json', 'w', encoding='utf-8') as f:
    json.dump(dados_finais, f, ensure_ascii=False, indent=2)

# Salvar YAML
yaml_content = yaml.dump(dados_finais, allow_unicode=True, sort_keys=False, default_flow_style=False)
with open('dados_finais_trma.yaml', 'w', encoding='utf-8') as f:
    f.write(yaml_content)

print("✅ Dados finais criados SEM PLANOS e SEM CTA!")
print("\n📊 Estrutura final:")
print("   ✓ Posicionamento")
print("   ✓ Métricas (8 métricas atualizadas)")
print("   ✓ 8 Empresas do Ecossistema")
print("   ✓ 4 Diferenciais")
print("   ✓ Tecnologia (4 items)")
print("   ✓ Visão Global (6 pilares)")
print("   ✓ Tráfego Pago (3 estratégias)")
print("   ✓ Cultura (frases de impacto)")
print("   ✓ Footer: © 2025 The Real Marketing Agency — All rights reserved.")
print("\n❌ REMOVIDO:")
print("   ✗ Planos Sob Medida (Starter, Growth, Enterprise)")
print("   ✗ Seção Diagnóstico Gratuito")
print("   ✗ Formulários de contato")
print("   ✗ CTAs de venda")
print("   ✗ Bônus exclusivos")
