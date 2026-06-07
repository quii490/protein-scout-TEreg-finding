---
type: protein-evaluation
gene: "FAM186A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM186A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM186A |
| 蛋白名称 | Protein FAM186A |
| 蛋白大小 | 2351 aa / 262.8 kDa |
| UniProt ID | A6NE01 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM186A/IF_images/MCF-7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM186A/IF_images/RT-4_1.jpg|RT-4]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; 额外: Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 2/10 | ×1 | 2 | 2351 aa / 262.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR049146, IPR049144, IPR049147; Pfam: PF20865, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Novel significant stage-specific differentially expressed genes in hepatocellular carcinoma.. *BMC cancer*. PMID: 31277598
2. DUSP5 and PHLDA1 mutations in mature cystic teratomas of the ovary identified on whole-exome sequencing may explain teratoma characteristics.. *Human genomics*. PMID: 36289533
3. Recurrent Coding Sequence Variation Explains Only A Small Fraction of the Genetic Architecture of Colorectal Cancer.. *Scientific reports*. PMID: 26553438
4. Whole exome sequencing and rare variant association study to identify genetic modifiers, KLF1 mutations, and a novel double mutation in Thai patients with hemoglobin E/beta-thalassemia.. *Hematology (Amsterdam, Netherlands)*. PMID: 36939018

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.3 |
| 高置信度残基 (pLDDT>90) 占比 | 1.1% |
| 置信残基 (pLDDT 70-90) 占比 | 29.7% |
| 中等置信 (pLDDT 50-70) 占比 | 15.5% |
| 低置信 (pLDDT<50) 占比 | 53.6% |
| 有序区域 (pLDDT>70) 占比 | 30.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM186A/FAM186A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=50.3），有序残基占 30.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049146, IPR049144, IPR049147; Pfam: PF20865, PF20870, PF20869 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAM47C | 0.573 | 0.095 | — |
| GOLGA6L2 | 0.517 | 0.099 | — |
| FAM170B | 0.475 | 0.092 | — |
| FER1L6 | 0.447 | 0.000 | — |
| TMPRSS15 | 0.435 | 0.094 | — |
| ZNF850 | 0.434 | 0.091 | — |
| UTP23 | 0.433 | 0.067 | — |
| OR2T4 | 0.420 | 0.045 | — |
| EFCAB5 | 0.409 | 0.095 | — |
| DIP2B | 0.408 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMARCB1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-26463|pubmed:30108113 |
| RYBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:34316702|imex:IM-29168 |
| Ppp1r13l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:37284462|imex:IM-29688 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 3
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.3 + PDB: 无 | pLDDT=50.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Vesicles; 额外: Plasma membrane | 待确认 |
| PPI | STRING + IntAct | 11 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM186A — Protein FAM186A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2351 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=50.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NE01
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185958-FAM186A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM186A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NE01
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM186A/FAM186A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NE01 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR049146;IPR049144;IPR049147; |
| Pfam | PF20865;PF20870;PF20869; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185958-FAM186A/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
