---
type: protein-evaluation
gene: "YIPF5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YIPF5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YIPF5 / FINGER5, YIP1A |
| 蛋白名称 | Protein YIPF5 |
| 蛋白大小 | 257 aa / 28.0 kDa |
| UniProt ID | Q969M3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum, Golgi apparatus, Vesicles; 额外: Nucleo; UniProt: Endoplasmic reticulum membrane; Golgi apparatus, cis-Golgi n |
| 蛋白大小 | 10/10 | ×1 | 10 | 257 aa / 28.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045231, IPR006977; Pfam: PF04893 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Golgi apparatus, Vesicles; 额外: Nucleoplasm | Supported |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus, cis-Golgi network membrane; Cytoplasmic vesicle, CO... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- COPII-coated ER to Golgi transport vesicle (GO:0030134)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum exit site (GO:0070971)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- trans-Golgi network (GO:0005802)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FINGER5, YIP1A |

**关键文献**:
1. YIPF5 mutations cause neonatal diabetes and microcephaly through endoplasmic reticulum stress.. *The Journal of clinical investigation*. PMID: 33164986
2. YIPF5 is an essential host factor for porcine epidemic diarrhea virus double-membrane vesicle formation.. *Journal of virology*. PMID: 40422075
3. Recessive TMEM167A variants cause neonatal diabetes, microcephaly, and epilepsy syndrome.. *The Journal of clinical investigation*. PMID: 40924476
4. A dual enhancer-silencer element, DES-K16, in mouse spermatocyte-derived GC-2spd(ts) cells.. *Biochemical and biophysical research communications*. PMID: 33121685
5. The microcephaly-associated protein YIPF5 differentially regulates ER export.. *iScience*. PMID: 41717013

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 20.2% |
| 置信残基 (pLDDT 70-90) 占比 | 31.1% |
| 中等置信 (pLDDT 50-70) 占比 | 16.0% |
| 低置信 (pLDDT<50) 占比 | 32.7% |
| 有序区域 (pLDDT>70) 占比 | 51.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 51.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045231, IPR006977; Pfam: PF04893 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STING1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| Unc93b1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| H9A910 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| YIF1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| RAB5C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RAB7A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cep131 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cdc16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 无 | pLDDT=67.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus, c / Endoplasmic reticulum, Golgi apparatus, Vesicles;  | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. YIPF5 — Protein YIPF5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小257 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q969M3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145817-YIPF5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YIPF5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969M3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (supported)。来源: https://www.proteinatlas.org/ENSG00000145817-YIPF5/subcellular

![](https://images.proteinatlas.org/42338/1543_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/42338/1543_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/42338/1544_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/42338/1544_B5_4_red_green.jpg)
![](https://images.proteinatlas.org/42338/1683_B6_14_cr580538c42938d_red_green.jpg)
![](https://images.proteinatlas.org/42338/1683_B6_17_cr580538ccbc004_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q969M3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
