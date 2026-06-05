---
type: protein-evaluation
gene: "SAPCD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SAPCD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SAPCD2 / C9orf140 |
| 蛋白名称 | Suppressor APC domain-containing protein 2 |
| 蛋白大小 | 394 aa / 42.6 kDa |
| UniProt ID | Q86UD0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Nucleoli; UniProt: Cytoplasm; Nucleus; Cytoplasm, cell cortex; Apical cell memb |
| 蛋白大小 | 10/10 | ×1 | 10 | 394 aa / 42.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026828, IPR057953; Pfam: PF25825, PF11414 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nucleoli | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, cell cortex; Apical cell membrane; Cell junction, tight junction | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- apical cortex (GO:0045179)
- apical junction complex (GO:0043296)
- apical plasma membrane (GO:0016324)
- bicellular tight junction (GO:0005923)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf140 |

**关键文献**:
1. The Function and Regulation of SAPCD2 in Physiological and Oncogenic Processes.. *Journal of Cancer*. PMID: 35517423
2. Comprehensive Bioinformatics Analyses and Experimental Validation of the Cell Cycle Related Protein SAPCD2 as a New Biomarker and Potential Therapeutic Target in Pancreatic Cancer.. *Journal of inflammation research*. PMID: 40034688
3. Homologous proteins SAPCD2X1 and SAPCD2 have significantly different carcinogenic capacities in human colorectal cancer cells based on structural prediction and functional verification.. *Cellular and molecular biology (Noisy-le-Grand, France)*. PMID: 38158695
4. SAPCD2 promotes invasiveness and migration ability of breast cancer cells via YAP/TAZ.. *European review for medical and pharmacological sciences*. PMID: 32329855
5. Gene signature to predict prognostic survival of hepatocellular carcinoma.. *Open medicine (Warsaw, Poland)*. PMID: 35071775

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.0 |
| 高置信度残基 (pLDDT>90) 占比 | 31.2% |
| 置信残基 (pLDDT 70-90) 占比 | 17.0% |
| 中等置信 (pLDDT 50-70) 占比 | 16.2% |
| 低置信 (pLDDT<50) 占比 | 35.5% |
| 有序区域 (pLDDT>70) 占比 | 48.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.0），有序残基占 48.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026828, IPR057953; Pfam: PF25825, PF11414 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLIN5 | 0.558 | 0.558 | — |
| MISP | 0.523 | 0.000 | — |
| GPSM1 | 0.484 | 0.483 | — |
| CDCA5 | 0.462 | 0.000 | — |
| AXIN1 | 0.446 | 0.000 | — |
| PIMREG | 0.438 | 0.000 | — |
| PROSER2 | 0.425 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cep350 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| RASSF9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| DEPDC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TANK | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| RALBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| VCL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYSRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GMNN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BFSP2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AIRIM | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 15
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.0 + PDB: 无 | pLDDT=68.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, cell cortex; Apical / Cytosol; 额外: Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 7 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SAPCD2 — Suppressor APC domain-containing protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小394 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UD0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186193-SAPCD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAPCD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UD0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000186193-SAPCD2/subcellular

![](https://images.proteinatlas.org/44154/562_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44154/562_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44154/568_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44154/568_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44154/575_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44154/575_G2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86UD0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
