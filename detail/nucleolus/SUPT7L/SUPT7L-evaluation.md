---
type: protein-evaluation
gene: "SUPT7L"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUPT7L 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SUPT7L / STAF65gamma|KIAA0764|SPT7L|STAF65 |
| 蛋白全称 | STAGA complex 65 subunit gamma |
| 蛋白大小 | 414 aa |
| UniProt ID | O94864 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SUPT7L/IF_images/Rh30_1.jpg|Rh30]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SUPT7L/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 414 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 5 篇，极度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: histone-fold |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **143/183** |  |
| **归一化总分** |  |  | **78.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 414 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 5 |

**评价**: PubMed 5 篇，极度新颖

**关键文献**:
1. Won HS et al. (2025). "Spatial gene expression profiling identifies prognostic features of residual tumors after neoadjuvant chemotherapy in triple-negative breast cancer". *Front Oncol*. PMID: 40900789
2. Hermán-Sánchez N et al. (2026). "Aspartyl-tRNA synthetase 1 (DARS1) reshapes hepatocellular carcinoma proteome and promotes aggressiveness through non-canonical SAGA-MYC signalling modulation". *Hepatology*. PMID: 41790991
3. Kopp J et al. (2024). "Loss-of-function variants affecting the STAGA complex component SUPT7L cause a developmental disorder with generalized lipodystrophy". *Hum Genet*. PMID: 38592547
4. Dong Z et al. (2018). "Oncogenomic analysis identifies novel biomarkers for tumor stage mycosis fungoides". *Medicine (Baltimore)*. PMID: 29794791
5. Royal T et al. (2026). "Neuroinflammatory and functional outcomes after TBI are sex-dependent: Lessons from estrous-phase stratified female mice". *Neurochem Int*. PMID: 41791496
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 414 aa |
| PDB 条数 | 3 |
| 已注释结构域 | 5 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SUPT7L/SUPT7L-PAE.png]]

**评价**: 3 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | BTP |
| InterPro | Histone-fold |
| InterPro | SUPT7L/Spt7 |
| Pfam | Bromo_TP |
| SMART | BTP |

**染色质调控潜力分析**: 染色质/DNA 结构域: histone-fold

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:SAGA complex (GO:0000124, IDA:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 3 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 5 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 5 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 3 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SUPT7L
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119760-SUPT7L
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SUPT7L%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O94864
- STRING: https://string-db.org/network/9606.ENSG00000119760
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94864


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SUPT7L-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/SUPT7L/SUPT7L-PAE.png]]




