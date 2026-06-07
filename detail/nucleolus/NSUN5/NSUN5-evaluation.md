---
type: protein-evaluation
gene: "NSUN5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NSUN5 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NSUN5 / NOL1R|p120(NOL1)|FLJ10267|NSUN5A|Ynl022cL |
| 蛋白名称 | 28S rRNA (cytosine-C(5))-methyltransferase |
| 蛋白大小 | 429 aa |
| UniProt ID | Q96P11 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NSUN5/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NSUN5/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | **24** | 核+胞质均衡，UniProt 支持核定位 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 429 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 57篇，有一定研究空间 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 10 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.0** | 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
| **原始总分** |  |  | **114.5/183** |  |
| **归一化总分** |  |  | **62.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus, nucleolus | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |

**结论**: 核+胞质均衡，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 429 aa，429 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 57 |
| 核定位分数 (weighted max) | 5 |
| Research hotness | 3.9125 |

**关键文献**:
1. Wu et al. (2024). "NSUN5/TET2-directed chromatin-associated RNA modification of 5-methylcytosine to 5-hydroxymethylcytosine governs glioma immune evasion.". *Proc Natl Acad Sci U S A*. PMID: 38547058
2. Han et al. (2025). "NSUN5 Facilitates Hepatocellular Carcinoma Progression by Increasing SMAD3 Expression.". *Adv Sci (Weinh)*. PMID: 39531371
3. Zhang et al. (2023). "Identification and validation of key biomarkers based on RNA methylation genes in sepsis.". *Front Immunol*. PMID: 37701433
4. Zhang et al. (2023). "CDK13 promotes lipid deposition and prostate cancer progression by stimulating NSUN5-mediated m5C modification of ACC1 mRNA.". *Cell Death Differ*. PMID: 37845385
5. Huang et al. (2025). "Nop2/Sun domain family member 5 contributes to tumorigenic properties in prostate cancer by engaging the PI3K-AKT pathway and tumor-associated macrophages.". *Biochim Biophys Acta Mol Basis Dis*. PMID: 40633812
**评价**: PubMed 57篇，有一定研究空间

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 429 aa |
| PDB 条目数 | 1 |
| UniProt 注释结构域数 | 10 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NSUN5/NSUN5-PAE.png]]

**评价**: 1 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | MeTrfase_RsmB-F_NOP2_cat |
| InterPro | MeTrfase_RsmB-F_NOP2_dom |
| InterPro | NSUN5_7_fdxn-like |
| InterPro | NSUN5_RCM1_N |
| InterPro | RCMT |
| InterPro | SAM-dependent_MTases_sf |
| Pfam | Methyltr_RsmB-F |
| Pfam | NSUN5_fdxn-like |
| Pfam | NSUN5_N |
| PROSITE | SAM_MT_RSMB_NOP |

**染色质调控潜力分析**: 10 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NSUN3 | 0 |  | 否 |
| NSUN4 | 0 |  | 否 |
| TRDMT1 | 0 |  | 否 |
| NOC4L | 0 |  | 否 |
| TRIM50 | 0 |  | 否 |
| BUD23 | 0 |  | 否 |
| NSUN6 | 0 |  | 否 |
| FBL | 0 |  | 否 |
| WDR74 | 0 |  | 否 |
| FKBP6 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 10 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. 新颖性: PubMed 57 篇，有一定研究空间
2. 核定位: 部分核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 1 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NSUN5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130305-NSUN5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NSUN5%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96P11
- STRING: https://string-db.org/network/9606.ENSG00000130305
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96P11


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NSUN5-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/NSUN5/NSUN5-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96P11 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR049560;IPR001678;IPR049561;IPR048889;IPR023267;IPR029063; |
| Pfam | PF01189;PF21148;PF21153; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000130305-NSUN5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCNF | Biogrid | false |
| FKBP5 | Opencell | false |
| MYC | Biogrid | false |
| NCAPH | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
