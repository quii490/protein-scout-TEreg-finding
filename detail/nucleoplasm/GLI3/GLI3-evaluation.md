---
type: protein-evaluation
gene: "GLI3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLI3 — REJECTED (研究热度过高 (PubMed strict=813，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLI3 |
| 蛋白名称 | Transcriptional activator GLI3 |
| 蛋白大小 | 1580 aa / 169.9 kDa |
| UniProt ID | P10071 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Vesicles; UniProt: Nucleus; Cytoplasm; Cell projection, cilium |
| 蛋白大小 | 5/10 | ×1 | 5 | 1580 aa / 169.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=813 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.4; PDB: 4BLD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043359, IPR056436, IPR036236, IPR013087; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.5/180** | |
| **归一化总分** | | | **41.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm; Cell projection, cilium | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- ciliary base (GO:0097546)
- ciliary tip (GO:0097542)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- GLI-SUFU complex (GO:1990788)
- nuclear speck (GO:0016607)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 813 |
| PubMed broad count | 1361 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Inferring and perturbing cell fate regulomes in human brain organoids.. *Nature*. PMID: 36198796
2. An inherited predisposition allele promotes gastric cancer via enhancing deubiquitination-mediated activation of epithelial-to-mesenchymal transition signaling.. *The Journal of clinical investigation*. PMID: 39998882
3. Germline-Somatic Liaison Dictates Cancer Subtypes via de novo Steroid Biosynthesis.. *Cancer discovery*. PMID: 40512155
4. Genetic Insights Into Hypothalamic Hamartoma: Unraveling Somatic Variants.. *Neurology. Genetics*. PMID: 39246740
5. Pallister-Hall syndrome, GLI3, and kidney malformation.. *American journal of medical genetics. Part C, Seminars in medical genetics*. PMID: 36165461

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.4 |
| 高置信度残基 (pLDDT>90) 占比 | 2.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 83.3% |
| 有序区域 (pLDDT>70) 占比 | 13.3% |
| 可用 PDB 条目 | 4BLD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=42.4），有序残基占 13.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043359, IPR056436, IPR036236, IPR013087; Pfam: PF00096, PF23561 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUFU | 0.999 | 0.867 | — |
| KIF7 | 0.995 | 0.458 | — |
| SPOP | 0.994 | 0.877 | — |
| BTRC | 0.991 | 0.710 | — |
| PTCH1 | 0.989 | 0.150 | — |
| SMO | 0.975 | 0.275 | — |
| SHH | 0.966 | 0.126 | — |
| PRKACB | 0.963 | 0.096 | — |
| PRKACG | 0.963 | 0.096 | — |
| PRKACA | 0.963 | 0.096 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STK36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:10806483 |
| SUFU | psi-mi:"MI:0096"(pull down) | pubmed:10564661|imex:IM-19149 |
| Pias1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14611647|imex:IM-16925 |
| Q74X18 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SMAD1 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |
| TOMM20 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SKIL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24819706|imex:IM-27580 |
| CEP44 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| KLHL7 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| RCCD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.4 + PDB: 4BLD | pLDDT=42.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell projection, cilium / Nucleoplasm; 额外: Nucleoli, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GLI3 — Transcriptional activator GLI3，研究基础较多，新颖性有限。
2. 蛋白大小1580 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 813 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=42.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 813 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P10071
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106571-GLI3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLI3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P10071
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000106571-GLI3/subcellular

![](https://images.proteinatlas.org/5534/1975_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/5534/1975_H4_3_red_green.jpg)
![](https://images.proteinatlas.org/5534/2120_F2_29_red_green.jpg)
![](https://images.proteinatlas.org/5534/2120_F2_42_red_green.jpg)
![](https://images.proteinatlas.org/5534/2131_G9_58_red_green.jpg)
![](https://images.proteinatlas.org/5534/2131_G9_80_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P10071-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P10071 |
| SMART | SM00355; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043359;IPR056436;IPR036236;IPR013087; |
| Pfam | PF00096;PF23561; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106571-GLI3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| STK36 | Intact, Biogrid | true |
| SUFU | Intact, Biogrid | true |
| AR | Biogrid | false |
| BTRC | Biogrid | false |
| CREBBP | Biogrid | false |
| CSNK2A2 | Opencell | false |
| KIF7 | Biogrid | false |
| MED12 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
