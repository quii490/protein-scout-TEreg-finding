---
type: protein-evaluation
gene: "TOX2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TOX2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TOX2 / dJ1108D11.2|GCX-1 |
| 蛋白全称 | TOX high mobility group box family member 2 |
| 蛋白大小 | 488 aa |
| UniProt ID | Q96NM4 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 488 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 54 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: hmg, hmg_box, hmg_box_2, hmg_box_dom, hmg_box_dom_sf |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **117/183** |  |
| **归一化总分** |  |  | **63.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TOX2/IF_images/A-431_HPA049900_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TOX2/IF_images/PC-3_HPA049900_2.jpg|PC-3]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 488 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 54 |

**评价**: PubMed 54 篇，中等研究热度

**关键文献**:
1. Zhou J et al. (2023). "Super-enhancer-driven TOX2 mediates oncogenesis in Natural Killer/T Cell Lymphoma". *Mol Cancer*. PMID: 37032358
2. He S et al. (2025). "Systemic immune activity occurs during human immune system maturation". *Cell*. PMID: 41161316
3. Seo H et al. (2019). "TOX and TOX2 transcription factors cooperate with NR4A transcription factors to impose CD8(+) T cell exhaustion". *Proc Natl Acad Sci U S A*. PMID: 31152140
4. Das A et al. (2024). "Transcription factor Tox2 is required for metabolic adaptation and tissue residency of ILC3 in the gut". *Immunity*. PMID: 38677292
5. Li A et al. (2024). "TOX2 nuclear-cytosol translocation is linked to leukemogenesis of acute T-cell leukemia by repressing TIM3 transcription". *Cell Death Differ*. PMID: 39080376
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 488 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TOX2/TOX2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HMG_box_dom |
| InterPro | HMG_box_dom_sf |
| InterPro | TOX_HMG-box_domain |
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

- F:chromatin DNA binding (GO:0031490, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 6 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 54 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TOX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124191-TOX2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TOX2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96NM4
- STRING: https://string-db.org/network/9606.ENSG00000124191
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96NM4


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TOX2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TOX2/TOX2-PAE.png]]




