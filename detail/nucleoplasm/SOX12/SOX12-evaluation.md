---
type: protein-evaluation
gene: "SOX12"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SOX12 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SOX12 / -- |
| 蛋白全称 | Transcription factor SOX-12 |
| 蛋白大小 | 315 aa |
| UniProt ID | O15370 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 315 aa，处于理想范围 |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed 100 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: hmg, hmg_box, hmg_box_2, hmg_box_dom, hmg_box_dom_sf |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **97/183** | **96.0/183** |  |  |  |
|  | **归一化总分** |  | **53.0/100** | **52.5/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SOX12/IF_images/A-549_HPA055052_1.jpg|A-549]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SOX12/IF_images/Hep-G2_HPA055052_2.jpg|Hep-G2]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 315 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 100 |

**评价**: PubMed 100 篇，中等研究热度

**关键文献**:
1. Luo X et al. (2024). "SOX12 Facilitates Hepatocellular Carcinoma Progression and Metastasis through Promoting Regulatory T-Cells Infiltration and Immunosuppression". *Adv Sci (Weinh)*. PMID: 39072947
2. Ruan X et al. (2025). "The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma". *Cell Death Dis*. PMID: 40593465
3. Liu X et al. (2024). "FOXP4 Is a Direct YAP1 Target That Promotes Gastric Cancer Stemness and Drives Metastasis". *Cancer Res*. PMID: 39047223
4. Zhang ZH et al. (2025). "SOX12 promotes serine synthesis and tumor progression in endometrial cancer". *Cell Signal*. PMID: 40379232
5. Huang W et al. (2015). "Sox12, a direct target of FoxQ1, promotes hepatocellular carcinoma metastasis through up-regulating Twist1 and FGFBP1". *Hepatology*. PMID: 25704764
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 315 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SOX12/SOX12-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HMG_box_dom |
| InterPro | HMG_box_dom_sf |
| InterPro | SOX-12/11/4 |
| InterPro | SRY-related_HMG-box_TF-like |
| Pfam | HMG_box |
| SMART | HMG |
| PROSITE | HMG_BOX_2 |

**染色质调控潜力分析**: 染色质/DNA 结构域: hmg, hmg_box, hmg_box_2, hmg_box_dom, hmg_box_dom_sf

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:chromatin (GO:0000785, ISA:NTNU_SB)
- C:protein-DNA complex (GO:0032993, IEA:Ensembl)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 7 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 100 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SOX12
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177732-SOX12
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SOX12%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O15370
- STRING: https://string-db.org/network/9606.ENSG00000177732
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15370


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SOX12-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SOX12/SOX12-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000177732-SOX12/subcellular

![](https://images.proteinatlas.org/55052/1334_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/55052/1334_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/55052/873_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/55052/873_D9_5_red_green.jpg)
![](https://images.proteinatlas.org/55052/878_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/55052/878_D9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15370 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR017386;IPR050140; |
| Pfam | PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177732-SOX12/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
