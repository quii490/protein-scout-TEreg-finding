---
type: protein-evaluation
gene: "BIRC2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BIRC2 — REJECTED (研究热度过高 (PubMed strict=161，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BIRC2 / API1, MIHB, RNF48 |
| 蛋白名称 | Baculoviral IAP repeat-containing protein 2 |
| 蛋白大小 | 618 aa / 69.9 kDa |
| UniProt ID | Q13490 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center, Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 618 aa / 69.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=161 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.6; PDB: 1QBH, 2L9M, 3D9T, 3D9U, 3M1D, 3MUP, 3OZ1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001370, IPR048875, IPR041933, IPR001315, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- CD40 receptor complex (GO:0035631)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- XY body (GO:0001741)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 161 |
| PubMed broad count | 401 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: API1, MIHB, RNF48 |

**关键文献**:
1. BIRC2 blockade facilitates immunotherapy of hepatocellular carcinoma.. *Molecular cancer*. PMID: 40223121
2. Genetic and Epigenetic Regulation of the Innate Immune Response to Gout.. *Immunological investigations*. PMID: 36745138
3. Gemcitabine resistance by CITED4 upregulation via the regulation of BIRC2 expression in pancreatic cancer.. *Journal of biomedical science*. PMID: 40389954
4. Prognostic Significance of the BIRC2-BIRC3 Gene Signature in Head and Neck Squamous Cell Carcinoma.. *Cancer genomics & proteomics*. PMID: 35985688
5. NAP1L1 regulates BIRC2 ubiquitination modification via E3 ubiquitin ligase UBR4 and hence determines hepatocellular carcinoma progression.. *Cell death discovery*. PMID: 38538582

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.6 |
| 高置信度残基 (pLDDT>90) 占比 | 38.8% |
| 置信残基 (pLDDT 70-90) 占比 | 36.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 19.6% |
| 有序区域 (pLDDT>70) 占比 | 75.5% |
| 可用 PDB 条目 | 1QBH, 2L9M, 3D9T, 3D9U, 3M1D, 3MUP, 3OZ1, 3T6P, 3UW4, 4EB9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1QBH, 2L9M, 3D9T, 3D9U, 3M1D, 3MUP, 3OZ1, 3T6P, 3UW4, 4EB9）+ AlphaFold极高置信度预测（pLDDT=76.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001370, IPR048875, IPR041933, IPR001315, IPR011029; Pfam: PF00653, PF00619, PF21290 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TNF | 0.999 | 0.994 | — |
| TRADD | 0.999 | 0.994 | — |
| TRAF2 | 0.999 | 0.993 | — |
| TRAF3 | 0.999 | 0.705 | — |
| RIPK1 | 0.999 | 0.893 | — |
| DIABLO | 0.999 | 0.950 | — |
| TRAF1 | 0.999 | 0.866 | — |
| TRAF5 | 0.999 | 0.066 | — |
| TNFRSF1A | 0.999 | 0.994 | — |
| DIABLO-2 | 0.999 | 0.876 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000477613.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| Traf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| TNFRSF1A | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:8943045 |
| JUP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TNF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12887920 |
| CASP8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12887920 |
| CASP7 | psi-mi:"MI:0096"(pull down) | pubmed:11084335 |
| CASP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:11084335 |
| CASP3 | psi-mi:"MI:0415"(enzymatic study) | pubmed:11084335 |
| MAGEA11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.6 + PDB: 1QBH, 2L9M, 3D9T, 3D9U, 3M1D,  | pLDDT=76.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoli fibrillar center, Cytosol; 额外: Nucleoplas | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. BIRC2 — Baculoviral IAP repeat-containing protein 2，研究基础较多，新颖性有限。
2. 蛋白大小618 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 161 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 161 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13490
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110330-BIRC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BIRC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13490
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000110330-BIRC2/subcellular

![](https://images.proteinatlas.org/20661/611_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/20661/611_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/20661/614_G7_3_red_green.jpg)
![](https://images.proteinatlas.org/20661/614_G7_4_red_green.jpg)
![](https://images.proteinatlas.org/20661/618_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/20661/618_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13490-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13490 |
| SMART | SM00238;SM00114;SM00184; |
| UniProt Domain [FT] | DOMAIN 453..543; /note="CARD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00046" |
| InterPro | IPR001370;IPR048875;IPR041933;IPR001315;IPR011029;IPR050784;IPR001841; |
| Pfam | PF00653;PF00619;PF21290;PF13920; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110330-BIRC2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BIRC7 | Intact, Biogrid, Bioplex | true |
| CASP7 | Intact, Biogrid | true |
| CASP9 | Intact, Biogrid | true |
| DIABLO | Intact, Biogrid | true |
| HTRA2 | Intact, Biogrid | true |
| NTAQ1 | Intact, Biogrid, Bioplex | true |
| OTUB1 | Intact, Biogrid | true |
| RAC1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
