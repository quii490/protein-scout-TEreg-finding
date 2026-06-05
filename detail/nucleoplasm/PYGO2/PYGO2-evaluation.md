---
type: protein-evaluation
gene: "PYGO2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PYGO2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PYGO2 / -- |
| 蛋白全称 | Pygopus homolog 2 |
| 蛋白大小 | 406 aa |
| UniProt ID | Q9BRQ0 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 406 aa，处于理想范围 |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed 94 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: phd, zf_phd_1, zf_phd_2, zinc_finger_phd-type_cs, znf_fyv |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **103/183** | **102.0/183** |  |  |  |
|  | **归一化总分** |  | **56.3/100** | **55.7/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PYGO2/IF_images/A-431_HPA023689_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PYGO2/IF_images/U-251MG_HPA023689_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 406 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 94 |

**评价**: PubMed 94 篇，中等研究热度

**关键文献**:
1. Chen Y et al. (2021). "Phosphorylation regulates cullin-based ubiquitination in tumorigenesis". *Acta Pharm Sin B*. PMID: 33643814
2. Jin J et al. (2025). "PYGO2 as a novel prognostic biomarker and its correlation with immune infiltrates in liver cancer". *Am J Clin Exp Immunol*. PMID: 40134825
3. Ling J et al. (2023). "Pygo2 activates BRPF1 via Pygo2-H3K4me2/3 interaction to maintain malignant progression in colon cancer". *Exp Cell Res*. PMID: 37423512
4. Chang W et al. (2025). "Pygo2+ T cells possess immunosuppressive features and inferior immunotherapeutic response in gastric cancer". *Front Immunol*. PMID: 40771810
5. Andrews PG & Kao KR (2016). "Wnt/β-catenin-dependent acetylation of Pygo2 by CBP/p300 histone acetyltransferase family members". *Biochem J*. PMID: 27647933
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 406 aa |
| PDB 条数 | 4 |
| 已注释结构域 | 10 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PYGO2/PYGO2-PAE.png]]

**评价**: 4 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Wnt_Signal_Transd_Protein |
| InterPro | Zinc_finger_PHD-type_CS |
| InterPro | Znf_FYVE_PHD |
| InterPro | Znf_PHD |
| InterPro | Znf_PHD-finger |
| InterPro | Znf_RING/FYVE/PHD |
| Pfam | PHD |
| SMART | PHD |
| PROSITE | ZF_PHD_1 |
| PROSITE | ZF_PHD_2 |

**染色质调控潜力分析**: 染色质/DNA 结构域: phd, zf_phd_1, zf_phd_2, zinc_finger_phd-type_cs, znf_fyve_phd

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:beta-catenin-TCF complex (GO:1990907, IDA:FlyBase)
- F:chromatin binding (GO:0003682, IEA:Ensembl)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 4 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 10 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 94 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 4 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PYGO2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163348-PYGO2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PYGO2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9BRQ0
- STRING: https://string-db.org/network/9606.ENSG00000163348
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BRQ0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PYGO2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PYGO2/PYGO2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000163348-PYGO2/subcellular

![](https://images.proteinatlas.org/23689/215_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/23689/215_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/23689/216_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/23689/216_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/23689/217_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/23689/217_D10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
