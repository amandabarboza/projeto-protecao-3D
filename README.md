# Projeto de proteção 3D

Modelo 3D interativo do pavimento tipo (Pav. 02) com os sistemas de proteção coletiva contra queda:

- **Guarda-corpo de madeira** nas sacadas, fachadas laterais e poço da escada do pavimento tipo, com as medidas tiradas na obra (altura 1,30 m, travessão do meio a 0,70 m, +15 cm de cada lado nas sacadas).
- **Guarda-corpo metálico** na periferia do pavimento de cima: 84 braços de 3,30 m a cada 1,20 m (posições do DWG) e painéis de tela de 2,96 × 1,20 m com rodapé interno de 17 cm.
- **Canteiro**: alvenaria de blocos de concreto, escoras de eucalipto, fôrma da laje, materiais e equipe com EPI (cinto paraquedista e linha de vida para trabalho em altura).

A página traz medidas editáveis, conferência com a NR-18 e quantitativo de materiais.

## Como abrir

Abra `index.html` no navegador. A página carrega o three.js pelo jsDelivr, então precisa de internet.

## Estrutura

| Pasta / arquivo | Conteúdo |
|---|---|
| `index.html` | Página pronta para abrir ou publicar (gerada) |
| `src/template.html` | Código-fonte da página, com os marcadores `__GEO__` e `__MET__` |
| `dados/geo.json` | Paredes, cômodos e linhas da camada 0 extraídos do DWG (coordenadas locais, em metros) |
| `dados/met.json` | Posições dos braços do guarda-corpo metálico e contorno da fachada |
| `scripts/` | Scripts de extração do DXF e de montagem da página |

## Como atualizar

1. Exporte o DWG para DXF (no AutoCAD, `DXFOUT`).
2. Extraia os dados (requer `pip install ezdxf`):
   ```bash
   python scripts/extrair_geometria.py Drawing1.dxf dados/geo.json
   python scripts/extrair_bracos.py dados/geo.json dados/met.json
   python scripts/agrupar_bracos.py dados/met.json
   ```
3. Gere a página:
   ```bash
   python scripts/montar_pagina.py
   ```

## Medidas estimadas

Duas medidas do braço metálico foram estimadas pelas fotos e precisam de conferência na obra: 0,60 m do pé do braço até o topo da parede e 0,40 m da garra superior até o 1º gancho. As duas podem ser ajustadas na página.
