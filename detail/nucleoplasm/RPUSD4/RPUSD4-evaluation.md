---
type: protein-evaluation
gene: "RPUSD4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RPUSD4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | RPUSD4 / FLJ14494 |
| 蛋白全称 | RNA pseudouridine synthase D4 | RNA pseudouridylate synthase domain containing 4 |
| 蛋白大小 | 377 aa |
| UniProt ID | Q96CM3 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 377 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 8 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | No annotated domains, 新颖蛋白基线水平 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.0** | None |
| **原始总分** |  |  | **114/183** |  |
| **归一化总分** |  |  | **62.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | N/A | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RPUSD4/IF_images/A-431_HPA039689_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RPUSD4/IF_images/U2OS_HPA039689_2.jpg|U2OS]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 377 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 8 |

**评价**: PubMed 8 篇，极度新颖

**关键文献**:
1. Martinez NM et al. (2022). "Pseudouridine synthases modify human pre-mRNA co-transcriptionally and affect pre-mRNA processing". *Mol Cell*. PMID: 35051350
2. Arroyo JD et al. (2016). "A Genome-wide CRISPR Death Screen Identifies Genes Essential for Oxidative Phosphorylation". *Cell Metab*. PMID: 27667664
3. Reyes A et al. (2020). "RCC1L (WBSCR16) isoforms coordinate mitochondrial ribosome assembly through their interaction with GTPases". *PLoS Genet*. PMID: 32735630
4. Antonicka H et al. (2017). "A pseudouridine synthase module is essential for mitochondrial protein synthesis and cell viability". *EMBO Rep*. PMID: 27974379
5. Chen Z et al. (2023). "Expression patterns of eight RNA-modified regulators correlating with immune infiltrates during the progression of osteoarthritis". *Front Immunol*. PMID: 37006267
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | N/A aa |
| PDB 条数 | 0 |
| 已注释结构域 | 0 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RPUSD4/RPUSD4-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|

**染色质调控潜力分析**: No annotated domains, 新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 0 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
--
**总计**: +0.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 8 篇，极度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RPUSD4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165526-RPUSD4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RPUSD4%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96CM3
- STRING: https://string-db.org/network/9606.ENSG00000165526
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96CM3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[RPUSD4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RPUSD4/RPUSD4-PAE.png]]




