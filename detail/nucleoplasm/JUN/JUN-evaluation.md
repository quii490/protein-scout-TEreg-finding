---
type: protein-evaluation
gene: "JUN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## JUN — REJECTED (研究热度过高 (PubMed strict=30229，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JUN |
| 蛋白名称 | Transcription factor Jun |
| 蛋白大小 | 331 aa / 35.7 kDa |
| UniProt ID | P05412 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 331 aa / 35.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=30229 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.2; PDB: 1A02, 1FOS, 1JNM, 1JUN, 1S9K, 1T2K, 5FV8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050946, IPR004827, IPR046347, IPR005643, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- euchromatin (GO:0000791)
- nuclear chromosome (GO:0000228)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)
- transcription factor AP-1 complex (GO:0035976)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30229 |
| PubMed broad count | 3921724 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Jun, an Oncological Foe or Friend?. *International journal of molecular sciences*. PMID: 39859271
2. Phorbol-12-myristate 13-acetate inhibits Nephronectin gene expression via Protein kinase C alpha and c-Jun/c-Fos transcription factors.. *Scientific reports*. PMID: 34645824
3. Encounters with Fos and Jun on the road to AP-1.. *Seminars in cancer biology*. PMID: 2133107
4. The Stress-response protein prostate-associated gene 4, interacts with c-Jun and potentiates its transactivation.. *Biochimica et biophysica acta*. PMID: 24263171
5. Mechanisms of regulation of oligodendrocyte development by p38 mitogen-activated protein kinase.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 20720108

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.2 |
| 高置信度残基 (pLDDT>90) 占比 | 19.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 32.6% |
| 低置信 (pLDDT<50) 占比 | 38.7% |
| 有序区域 (pLDDT>70) 占比 | 28.7% |
| 可用 PDB 条目 | 1A02, 1FOS, 1JNM, 1JUN, 1S9K, 1T2K, 5FV8, 5T01, 6Y3V, 8SOS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.2），有序残基占 28.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050946, IPR004827, IPR046347, IPR005643, IPR002112; Pfam: PF00170, PF03957 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK9 | 0.999 | 0.964 | — |
| FOS | 0.999 | 0.999 | — |
| MAPK8 | 0.999 | 0.997 | — |
| FOSB | 0.999 | 0.807 | — |
| FOSL2 | 0.999 | 0.956 | — |
| JUND | 0.999 | 0.860 | — |
| FOSL1 | 0.999 | 0.872 | — |
| JUNB | 0.999 | 0.639 | — |
| ESR1 | 0.999 | 0.631 | — |
| EP300 | 0.999 | 0.885 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP2K4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9808624|mint:MINT-65483 |
| MAP3K1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:9808624|mint:MINT-65483 |
| Q6FHM7 | psi-mi:"MI:0077"(nuclear magnetic resonance) | pubmed:8662824|imex:IM-27455 |
| BATF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EDF1 | psi-mi:"MI:0096"(pull down) | pubmed:10567391 |
| MAPK8 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-14535|pubmed:16291755 |
| MAPK9 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:16533805|imex:IM-18913 |
| KPNA2 | psi-mi:"MI:0096"(pull down) | imex:IM-15364|pubmed:21988832 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| HDGF | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.2 + PDB: 1A02, 1FOS, 1JNM, 1JUN, 1S9K,  | pLDDT=61.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. JUN — Transcription factor Jun，研究基础较多，新颖性有限。
2. 蛋白大小331 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30229 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 30229 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P05412
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177606-JUN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JUN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P05412
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000177606-JUN/subcellular

![](https://images.proteinatlas.org/3801/624_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/3801/624_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/3801/628_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/3801/628_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/3801/630_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/3801/630_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P05412-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
