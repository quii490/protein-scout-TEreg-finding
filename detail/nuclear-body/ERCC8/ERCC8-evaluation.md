---
type: protein-evaluation
gene: "ERCC8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ERCC8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERCC8 / CKN1, CSA |
| 蛋白名称 | DNA excision repair protein ERCC-8 |
| 蛋白大小 | 396 aa / 44.1 kDa |
| UniProt ID | Q13216 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/ERCC8/IF_images/A-549_1.jpg|A-549]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/ERCC8/IF_images/MCF-7_1.jpg|MCF-7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus; Chromosome; Nucleus matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 396 aa / 44.1 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=86 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.6; PDB: 4A11, 6FCV, 7OO3, 7OOB, 7OOP, 7OPC, 7OPD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR042238, IPR015943, IPR020472, IPR019775, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Nucleus; Chromosome; Nucleus matrix | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- Cul4-RING E3 ubiquitin ligase complex (GO:0080008)
- Cul4A-RING E3 ubiquitin ligase complex (GO:0031464)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleotide-excision repair complex (GO:0000109)
- nucleus (GO:0005634)
- perikaryon (GO:0043204)
- protein-containing complex (GO:0032991)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 86 |
| PubMed broad count | 197 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CKN1, CSA |

**关键文献**:
1. Cockayne Syndrome.. **. PMID: 20301516
2. Cockayne Syndrome.. **. PMID: 30252254
3. Shared Genetics and Comorbid Genes of Amyotrophic Lateral Sclerosis and Parkinson's Disease.. *Movement disorders : official journal of the Movement Disorder Society*. PMID: 37534731
4. Integrative genomic analysis implicates ERCC6 and its interaction with ERCC8 in susceptibility to breast cancer.. *Scientific reports*. PMID: 33277540
5. Associations of individual and joint expressions of ERCC6 and ERCC8 with clinicopathological parameters and prognosis of gastric cancer.. *PeerJ*. PMID: 34316408

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 86.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 6.3% |
| 有序区域 (pLDDT>70) 占比 | 92.2% |
| 可用 PDB 条目 | 4A11, 6FCV, 7OO3, 7OOB, 7OOP, 7OPC, 7OPD, 8B3D, 8B3F, 8B3G |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/ERCC8/ERCC8-PAE.png]]

**评价**: PDB实验结构（4A11, 6FCV, 7OO3, 7OOB, 7OOP, 7OPC, 7OPD, 8B3D, 8B3F, 8B3G）+ AlphaFold极高置信度预测（pLDDT=91.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042238, IPR015943, IPR020472, IPR019775, IPR036322; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL4A | 0.999 | 0.971 | — |
| ERCC6 | 0.999 | 0.986 | — |
| DDB1 | 0.999 | 0.989 | — |
| UVSSA | 0.998 | 0.977 | — |
| RBX1 | 0.994 | 0.921 | — |
| ERCC5 | 0.990 | 0.000 | — |
| CUL4B | 0.984 | 0.810 | — |
| ERCC1 | 0.977 | 0.000 | — |
| ERCC4 | 0.975 | 0.000 | — |
| POLR2A | 0.963 | 0.920 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| XAB2 | psi-mi:"MI:0096"(pull down) | pubmed:10944529 |
| CBR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UQCRQ | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ERCC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:7664335 |
| GTF2H2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:7664335 |
| COPS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Ddb1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL4A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 4A11, 6FCV, 7OO3, 7OOB, 7OOP,  | pLDDT=91.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Nucleus matrix / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ERCC8 — DNA excision repair protein ERCC-8，研究基础较多，新颖性有限。
2. 蛋白大小396 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 86 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13216
- Protein Atlas: https://www.proteinatlas.org/ENSG00000049167-ERCC8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERCC8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13216
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/ERCC8/ERCC8-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13216 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042238;IPR015943;IPR020472;IPR019775;IPR036322;IPR001680; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000049167-ERCC8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDB1 | Biogrid, Opencell | true |
| XAB2 | Intact, Biogrid | true |
| CCT2 | Biogrid | false |
| CCT3 | Biogrid | false |
| CCT4 | Biogrid | false |
| CCT5 | Biogrid | false |
| CCT6A | Biogrid | false |
| CCT8 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
