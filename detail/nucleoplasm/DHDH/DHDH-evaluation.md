---
type: protein-evaluation
gene: "DHDH"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DHDH 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHDH / 2DD |
| 蛋白名称 | Trans-1,2-dihydrobenzene-1,2-diol dehydrogenase |
| 蛋白大小 | 334 aa / 36.4 kDa |
| UniProt ID | Q9UQ10 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Actin filaments; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 36.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=98.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000683, IPR050984, IPR055170, IPR036291; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.5/180** | |
| **归一化总分** | | | **69.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Actin filaments | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: 2DD |

**关键文献**:
1. Dimeric dihydrodiol dehydrogenase is an efficient primate 1,5-anhydro-D-fructose reductase.. *Biochemical and biophysical research communications*. PMID: 32253031
2. Signature of immune-related metabolic genes predicts the prognosis of hepatocellular carcinoma.. *Frontiers in immunology*. PMID: 39654885
3. Common variants of the ALDH2 and DHDH genes and the risk of Dupuytren's disease.. *The Journal of hand surgery, European volume*. PMID: 23303836
4. Host genetics and gut microbiota jointly regulate blood biochemical indicators in chickens.. *Applied microbiology and biotechnology*. PMID: 37792060
5. [Characterization of D-lactate dehydrogenase isozymes from a D-lactic acid producing bacterium Sporolactobacillus inulinus].. *Wei sheng wu xue bao = Acta microbiologica Sinica*. PMID: 29741845

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 98.3 |
| 高置信度残基 (pLDDT>90) 占比 | 99.1% |
| 置信残基 (pLDDT 70-90) 占比 | 0.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=98.3，有序区 99.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000683, IPR050984, IPR055170, IPR036291; Pfam: PF01408, PF22725 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZNF185 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCP110 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATRN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SBF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ICAM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DNAJB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPOX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=98.3 + PDB: 无 | pLDDT=98.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Actin filaments | 待确认 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DHDH — Trans-1,2-dihydrobenzene-1,2-diol dehydrogenase，非常新颖，仅有少数基础研究。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UQ10
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104808-DHDH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHDH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UQ10
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000104808-DHDH/subcellular

![](https://images.proteinatlas.org/44131/498_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44131/498_D10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44131/501_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44131/501_D10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44131/512_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44131/512_D10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UQ10-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UQ10 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000683;IPR050984;IPR055170;IPR036291; |
| Pfam | PF01408;PF22725; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104808-DHDH/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARMCX5 | Bioplex | false |
| EIPR1 | Bioplex | false |
| FAM91A1 | Bioplex | false |
| HK2 | Bioplex | false |
| HKDC1 | Bioplex | false |
| HSPA2 | Bioplex | false |
| HSPA8 | Bioplex | false |
| ICAM1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
