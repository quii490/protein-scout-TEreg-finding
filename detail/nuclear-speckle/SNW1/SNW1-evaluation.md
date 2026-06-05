---
type: protein-evaluation
gene: "SNW1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SNW1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SNW1 / SKIIP, SKIP |
| 蛋白名称 | SNW domain-containing protein 1 |
| 蛋白大小 | 536 aa / 61.5 kDa |
| UniProt ID | Q13573 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 536 aa / 61.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.5; PDB: 5MQF, 5XJC, 5YZG, 5Z58, 6FF4, 6FF7, 6ICZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017862, IPR004015; Pfam: PF02731 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- catalytic step 2 spliceosome (GO:0071013)
- nuclear body (GO:0016604)
- nuclear matrix (GO:0016363)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spliceosomal complex (GO:0005681)
- U2-type catalytic step 2 spliceosome (GO:0071007)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 118 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SKIIP, SKIP |

**关键文献**:
1. Mutations in the spliceosomal gene SNW1 cause neurodevelopment disorders with microcephaly.. *The Journal of clinical investigation*. PMID: 40608414
2. Super-enhancer-driven LIF promotes the mesenchymal transition in glioblastoma by activating ITGB2 signaling feedback in microglia.. *Neuro-oncology*. PMID: 38554116
3. Antrodia cinnamomea triterpenoids attenuate cardiac hypertrophy via the SNW1/RXR/ALDH2 axis.. *Redox biology*. PMID: 39591904
4. Phosphorylation of SNW1 protein associated with equine melanocytic neoplasm identified in serum and feces.. *Scientific reports*. PMID: 39730520
5. Dexmedetomidine Inhibits NF-κB-Transcriptional Activity in Neurons Undergoing Ischemia-Reperfusion by Regulating O-GlcNAcylation of SNW1.. *Journal of neuropathology and experimental neurology*. PMID: 35818332

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.5 |
| 高置信度残基 (pLDDT>90) 占比 | 39.6% |
| 置信残基 (pLDDT 70-90) 占比 | 28.2% |
| 中等置信 (pLDDT 50-70) 占比 | 24.4% |
| 低置信 (pLDDT<50) 占比 | 7.8% |
| 有序区域 (pLDDT>70) 占比 | 67.8% |
| 可用 PDB 条目 | 5MQF, 5XJC, 5YZG, 5Z58, 6FF4, 6FF7, 6ICZ, 6ID0, 6ID1, 6QDV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5MQF, 5XJC, 5YZG, 5Z58, 6FF4, 6FF7, 6ICZ, 6ID0, 6ID1, 6QDV）+ AlphaFold极高置信度预测（pLDDT=78.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017862, IPR004015; Pfam: PF02731 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNRPA1 | 0.999 | 0.995 | — |
| CRNKL1 | 0.999 | 0.997 | — |
| PRPF8 | 0.999 | 0.997 | — |
| CWC22 | 0.999 | 0.983 | — |
| EFTUD2 | 0.999 | 0.995 | — |
| CDC40 | 0.999 | 0.997 | — |
| SNRPD2 | 0.999 | 0.988 | — |
| PRPF19 | 0.999 | 0.996 | — |
| PLRG1 | 0.999 | 0.995 | — |
| SYF2 | 0.999 | 0.995 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| prp45 | psi-mi:"MI:0018"(two hybrid) | pubmed:11414703 |
| cdc5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:11884590 |
| dre4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| prp17 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| prp19 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| cwf2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| EBI-2551848 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| RBPJ | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| NCOR2 | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| NOTCH1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10713164 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.5 + PDB: 5MQF, 5XJC, 5YZG, 5Z58, 6FF4,  | pLDDT=78.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SNW1 — SNW domain-containing protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小536 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13573
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100603-SNW1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SNW1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13573
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000100603-SNW1/subcellular

![](https://images.proteinatlas.org/17370/140_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/17370/140_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/17370/173_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/17370/173_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/17370/1884_C12_13_cr5b98d2156e58f_red_green.jpg)
![](https://images.proteinatlas.org/17370/1884_C12_2_cr5b98d2156e559_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13573-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
