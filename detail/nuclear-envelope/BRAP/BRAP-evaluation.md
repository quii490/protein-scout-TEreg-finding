---
type: protein-evaluation
gene: "BRAP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRAP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRAP / RNF52 |
| 蛋白名称 | BRCA1-associated protein |
| 蛋白大小 | 592 aa / 67.3 kDa |
| UniProt ID | Q7Z569 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nuclear membrane; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 592 aa / 67.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011422, IPR034932, IPR035979, IPR047243, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear membrane | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 347 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF52 |

**关键文献**:
1. Bombesin receptor-activated protein exacerbates cisplatin-induced AKI by regulating the degradation of SIRT2.. *Nephrology, dialysis, transplantation : official publication of the European Dialysis and Transplant Association - European Renal Association*. PMID: 35488871
2. BRCA1-Associated Protein Increases Invasiveness of Esophageal Squamous Cell Carcinoma.. *Gastroenterology*. PMID: 28780075
3. Brap regulates liver morphology and hepatocyte turnover via modulation of the Hippo pathway.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 35476518
4. BRCA1-associated protein induced proliferation and migration of gastric cancer cells through MAPK pathway.. *Surgical oncology*. PMID: 32890957
5. Role of BRCA1-associated protein (BRAP) variant in childhood pulmonary arterial hypertension.. *PloS one*. PMID: 30703135

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 30.7% |
| 置信残基 (pLDDT 70-90) 占比 | 41.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.5% |
| 低置信 (pLDDT<50) 占比 | 15.4% |
| 有序区域 (pLDDT>70) 占比 | 72.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.1，有序区 72.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011422, IPR034932, IPR035979, IPR047243, IPR001841; Pfam: PF07576, PF13639, PF02148 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRCA1 | 0.997 | 0.474 | — |
| KSR1 | 0.984 | 0.636 | — |
| UBB | 0.935 | 0.271 | — |
| HRAS | 0.930 | 0.314 | — |
| NRAS | 0.911 | 0.071 | — |
| KSR2 | 0.906 | 0.069 | — |
| MRAS | 0.903 | 0.058 | — |
| KRAS | 0.903 | 0.071 | — |
| RRAS | 0.901 | 0.058 | — |
| RRAS2 | 0.901 | 0.058 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| B4DRM1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:14724641 |
| BRCA1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9497340|mint:MINT-65476 |
| HRAS | psi-mi:"MI:0096"(pull down) | pubmed:14724641 |
| KSR1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:14724641 |
| DDB1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10777491 |
| UBE2H | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| TRIM8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| TRIM55 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| TRIM41 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 无 | pLDDT=76.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BRAP — BRCA1-associated protein，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小592 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z569
- Protein Atlas: https://www.proteinatlas.org/ENSG00000089234-BRAP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRAP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z569
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000089234-BRAP/subcellular

![](https://images.proteinatlas.org/40357/460_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/40357/460_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/40357/465_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/40357/465_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/40357/467_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/40357/467_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z569-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z569 |
| SMART | SM00184;SM00290; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011422;IPR034932;IPR035979;IPR047243;IPR001841;IPR013083;IPR001607; |
| Pfam | PF07576;PF13639;PF02148; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000089234-BRAP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKAP3 | Intact, Biogrid | true |
| BRCA1 | Intact, Biogrid | true |
| EFHC1 | Intact, Biogrid | true |
| CDC14A | Biogrid | false |
| DNMT1 | Biogrid | false |
| HMG20A | Biogrid | false |
| HRAS | Intact | false |
| KLHDC3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
