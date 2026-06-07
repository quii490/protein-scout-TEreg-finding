---
type: protein-evaluation
gene: "FOSB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOSB — REJECTED (研究热度过高 (PubMed strict=1200，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOSB / G0S3 |
| 蛋白名称 | Protein FosB |
| 蛋白大小 | 338 aa / 35.9 kDa |
| UniProt ID | P53539 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 338 aa / 35.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1200 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.1; PDB: 5VPA, 5VPB, 5VPC, 5VPD, 5VPE, 5VPF, 6UCI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1200 |
| PubMed broad count | 1899 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: G0S3 |

**关键文献**:
1. New kids on the block: FOS and FOSB gene.. *Journal of clinical pathology*. PMID: 37553246
2. Drug experience epigenetically primes Fosb gene inducibility in rat nucleus accumbens.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 22836260
3. Subgroup of meningiomas involving FOS and FOSB gene fusions.. *Nature communications*. PMID: 41298363
4. Platelet-Rich Plasma-Derived Exosome-Encapsulated Hydrogels Accelerate Diabetic Wound Healing by Inhibiting Fibroblast Ferroptosis.. *ACS applied materials & interfaces*. PMID: 40315047
5. Two-polarized roles of transcription factor FOSB in lung cancer progression and prognosis: dependent on p53 status.. *Journal of experimental & clinical cancer research : CR*. PMID: 39164746

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.1 |
| 高置信度残基 (pLDDT>90) 占比 | 18.6% |
| 置信残基 (pLDDT 70-90) 占比 | 4.7% |
| 中等置信 (pLDDT 50-70) 占比 | 26.0% |
| 低置信 (pLDDT<50) 占比 | 50.6% |
| 有序区域 (pLDDT>70) 占比 | 23.3% |
| 可用 PDB 条目 | 5VPA, 5VPB, 5VPC, 5VPD, 5VPE, 5VPF, 6UCI, 6UCL, 6UCM, 7UCC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.1），有序残基占 23.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JUN | 0.999 | 0.807 | — |
| JUNB | 0.999 | 0.728 | — |
| JUND | 0.999 | 0.964 | — |
| FOS | 0.999 | 0.359 | — |
| FOSL1 | 0.998 | 0.000 | — |
| FOSL2 | 0.998 | 0.000 | — |
| EGR1 | 0.987 | 0.066 | — |
| HDAC1 | 0.957 | 0.107 | — |
| EGR3 | 0.956 | 0.066 | — |
| EGR2 | 0.948 | 0.066 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| hflC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENKD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CREB5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| POU6F2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CENPO | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TENT5B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZC3H10 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FAM222B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| JUNB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FOXP3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.1 + PDB: 5VPA, 5VPB, 5VPC, 5VPD, 5VPE,  | pLDDT=59.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOSB — Protein FosB，研究基础较多，新颖性有限。
2. 蛋白大小338 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1200 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1200 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53539
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125740-FOSB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOSB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53539
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000125740-FOSB/subcellular

![](https://images.proteinatlas.org/54663/1486_C1_5_red_green.jpg)
![](https://images.proteinatlas.org/54663/1486_C1_6_red_green.jpg)
![](https://images.proteinatlas.org/54663/1496_C1_3_red_green.jpg)
![](https://images.proteinatlas.org/54663/1496_C1_4_red_green.jpg)
![](https://images.proteinatlas.org/54663/1534_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/54663/1534_B6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P53539-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P53539 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 155..218; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR000837;IPR004827;IPR046347; |
| Pfam | PF00170; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125740-FOSB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATF2 | Intact, Biogrid, Bioplex | true |
| JUN | Biogrid, Opencell, Bioplex | true |
| JUNB | Intact, Biogrid, Bioplex | true |
| MIDN | Biogrid, Bioplex | true |
| NFE2L2 | Intact, Biogrid | true |
| AGXT | Intact | false |
| CENPO | Intact | false |
| CREB5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
