---
type: protein-evaluation
gene: "ERG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERG — REJECTED (研究热度过高 (PubMed strict=4373，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERG |
| 蛋白名称 | Transcriptional regulator ERG |
| 蛋白大小 | 479 aa / 53.8 kDa |
| UniProt ID | P11308 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 479 aa / 53.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=4373 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.4; PDB: 1SXE, 4IRG, 4IRH, 4IRI, 5YBC, 5YBD, 6VGE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ribonucleoprotein complex (GO:1990904)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4373 |
| PubMed broad count | 14629 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. X-Linked Retinoschisis.. *Cold Spring Harbor perspectives in medicine*. PMID: 36690462
2. Gene of the month: ERG.. *Journal of clinical pathology*. PMID: 35738886
3. Germ line ERG haploinsufficiency defines a new syndrome with cytopenia and hematological malignancy predisposition.. *Blood*. PMID: 38991192
4. TMPRSS2-ERG activates NO-cGMP signaling in prostate cancer cells.. *Oncogene*. PMID: 30718921
5. The prognostic and predictive value of TMPRSS2-ERG gene fusion and ERG protein expression in prostate cancer biopsies.. *Danish medical journal*. PMID: 27910803

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.4 |
| 高置信度残基 (pLDDT>90) 占比 | 18.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 12.5% |
| 低置信 (pLDDT<50) 占比 | 54.3% |
| 有序区域 (pLDDT>70) 占比 | 33.2% |
| 可用 PDB 条目 | 1SXE, 4IRG, 4IRH, 4IRI, 5YBC, 5YBD, 6VGE, 6VGG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.4），有序残基占 33.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR036388; Pfam: PF00178, PF02198 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMPRSS2 | 0.933 | 0.194 | — |
| AR | 0.893 | 0.625 | — |
| RUNX2 | 0.862 | 0.840 | — |
| SETDB1 | 0.841 | 0.301 | — |
| CBFB | 0.821 | 0.809 | — |
| SRSF10 | 0.760 | 0.000 | — |
| EWSR1 | 0.754 | 0.000 | — |
| KCNH6 | 0.727 | 0.000 | — |
| SPOP | 0.703 | 0.510 | — |
| FUS | 0.680 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.4 + PDB: 1SXE, 4IRG, 4IRH, 4IRI, 5YBC,  | pLDDT=59.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ERG — Transcriptional regulator ERG，研究基础较多，新颖性有限。
2. 蛋白大小479 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4373 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 4373 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P11308
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157554-ERG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P11308
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000157554-ERG/subcellular

![](https://images.proteinatlas.org/18377/942_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/18377/942_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/18377/955_A4_3_red_green.jpg)
![](https://images.proteinatlas.org/18377/955_A4_4_red_green.jpg)
![](https://images.proteinatlas.org/18377/972_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/18377/972_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P11308-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P11308 |
| SMART | SM00413;SM00251; |
| UniProt Domain [FT] | DOMAIN 113..199; /note="PNT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00762" |
| InterPro | IPR000418;IPR046328;IPR003118;IPR013761;IPR036388;IPR036390; |
| Pfam | PF00178;PF02198; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157554-ERG/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AR | Intact, Biogrid | true |
| NFIA | Intact, Biogrid | true |
| NFIB | Intact, Biogrid | true |
| PARP1 | Intact, Biogrid | true |
| PIAS1 | Intact, Biogrid | true |
| SMARCE1 | Intact, Biogrid | true |
| ACTB | Biogrid | false |
| ADAR | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
