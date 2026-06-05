---
type: protein-evaluation
gene: "DACT3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DACT3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DACT3 / RRR1 |
| 蛋白名称 | Dapper homolog 3 |
| 蛋白大小 | 629 aa / 64.9 kDa |
| UniProt ID | Q96B18 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 629 aa / 64.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024843; Pfam: PF15268 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RRR1 |

**关键文献**:
1. Hypoxia-induced LncRNA DACT3-AS1 upregulates PKM2 to promote metastasis in hepatocellular carcinoma through the HDAC2/FOXA3 pathway.. *Experimental & molecular medicine*. PMID: 35764883
2. DACT3 has a tumor-inhibiting role in acute myeloid leukemia via the suppression of Wnt/β-catenin signaling by DVL2.. *Journal of biochemical and molecular toxicology*. PMID: 35187752
3. Identification of biological significance of different stages of varicose vein development based on mRNA sequencing.. *Scientific reports*. PMID: 39341975
4. DACT3-DVL1 Interaction-Mediated Canonical WNT Signaling Regulates Non-Small Cell Lung Cancer Progression and Cisplatin Resistance.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40838391
5. Butyrate mediates anti-inflammatory effects of Faecalibacterium prausnitzii in intestinal epithelial cells through Dact3.. *Gut microbes*. PMID: 33054518

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.5 |
| 高置信度残基 (pLDDT>90) 占比 | 6.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 19.9% |
| 低置信 (pLDDT<50) 占比 | 63.1% |
| 有序区域 (pLDDT>70) 占比 | 17.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.5），有序残基占 17.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024843; Pfam: PF15268 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DACT2 | 0.928 | 0.095 | — |
| DVL2 | 0.652 | 0.125 | — |
| CTNNB1 | 0.625 | 0.100 | — |
| EZH2 | 0.497 | 0.000 | — |
| AXIN1 | 0.489 | 0.000 | — |
| ZNF503 | 0.479 | 0.000 | — |
| TRAT1 | 0.477 | 0.477 | — |
| CDK13 | 0.473 | 0.000 | — |
| DVL1 | 0.456 | 0.125 | — |
| DACT1 | 0.453 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SESTD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZBTB21 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CBY1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| KCTD3 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| KIF13B | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| KSR1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| GIGYF1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PKD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRAT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SLC38A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.5 + PDB: 无 | pLDDT=52.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DACT3 — Dapper homolog 3，非常新颖，仅有少数基础研究。
2. 蛋白大小629 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=52.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96B18
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197380-DACT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DACT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96B18
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000197380-DACT3/subcellular

![](https://images.proteinatlas.org/43053/1222_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/43053/1222_E9_3_red_green.jpg)
![](https://images.proteinatlas.org/43053/465_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/43053/465_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/43053/467_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/43053/467_E7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96B18-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
