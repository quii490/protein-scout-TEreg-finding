---
type: protein-evaluation
gene: "PWWP2A"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PWWP2A 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PWWP2A / KIAA1935 |
| 蛋白全称 | PWWP domain-containing protein 2A |
| 蛋白大小 | 755 aa |
| UniProt ID | Q96N64 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 755 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 18 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: pwwp, pwwp_dom |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | UniProt + GO 核定位互证 (+1) |
| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PWWP2A/IF_images/CACO-2_HPA046733_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PWWP2A/IF_images/HeLa_HPA046733_2.jpg|HeLa]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 755 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 18 |

**评价**: PubMed 18 篇，极度新颖

**关键文献**:
1. Link S & Hake SB (2017). "PWWP2A: A novel mitosis link?". *Cell Cycle*. PMID: 28933988
2. Wunderlich TM et al. (2024). "ZNF512B binds RBBP4 via a variant NuRD interaction motif and aggregates chromatin in a NuRD complex-independent manner". *Nucleic Acids Res*. PMID: 39460621
3. Herchenröther A et al. (2023). "The H2A.Z and NuRD associated protein HMG20A controls early head and heart developmental transcription programs". *Nat Commun*. PMID: 36709316
4. Link S et al. (2018). "PWWP2A binds distinct chromatin moieties and interacts with an MTA1-specific core NuRD complex". *Nat Commun*. PMID: 30327463
5. Klubíčková N et al. (2024). "Comprehensive clinicopathological, molecular, and methylation analysis of mesenchymal tumors with NTRK and other kinase gene aberrations". *J Pathol*. PMID: 38332737
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 755 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 4 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PWWP2A/PWWP2A-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PWWP_dom |
| Pfam | PWWP |
| SMART | PWWP |
| PROSITE | PWWP |

**染色质调控潜力分析**: 染色质/DNA 结构域: pwwp, pwwp_dom

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- F:chromatin binding (GO:0003682, IDA:UniProtKB)
- F:NuRD complex binding (GO:0120325, IDA:UniProtKB)
- P:chromatin remodeling (GO:0006338, IMP:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 4 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 18 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PWWP2A
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170234-PWWP2A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PWWP2A%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96N64
- STRING: https://string-db.org/network/9606.ENSG00000170234
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96N64


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PWWP2A-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PWWP2A/PWWP2A-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170234-PWWP2A/subcellular

![](https://images.proteinatlas.org/46733/699_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/46733/699_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/46733/780_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/46733/780_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/46733/788_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/46733/788_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
