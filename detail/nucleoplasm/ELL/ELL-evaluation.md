---
type: protein-evaluation
gene: "ELL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ELL — REJECTED (研究热度过高 (PubMed strict=254，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELL / C19orf17 |
| 蛋白名称 | RNA polymerase II elongation factor ELL |
| 蛋白大小 | 621 aa / 68.3 kDa |
| UniProt ID | P55199 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: Nucleus; Nucleus speckle; Nucleus, Cajal body |
| 蛋白大小 | 10/10 | ×1 | 10 | 621 aa / 68.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=254 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 2DOA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042065, IPR031176, IPR019464, IPR010844, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Supported |
| UniProt | Nucleus; Nucleus speckle; Nucleus, Cajal body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cajal body (GO:0015030)
- cytosol (GO:0005829)
- euchromatin (GO:0000791)
- histone locus body (GO:0035363)
- nuclear body (GO:0016604)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- transcription elongation factor complex (GO:0008023)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 254 |
| PubMed broad count | 2310 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C19orf17 |

**关键文献**:
1. ELL and EAF1 are Cajal body components that are disrupted in MLL-ELL leukemia.. *Molecular biology of the cell*. PMID: 12686606
2. RNA polymerase II elongation factors use conserved regulatory mechanisms.. *Current opinion in structural biology*. PMID: 38181687
3. HBO1-MLL interaction promotes AF4/ENL/P-TEFb-mediated leukemogenesis.. *eLife*. PMID: 34431785
4. Negative Feedback Loop Mechanism between EAF1/2 and DBC1 in Regulating ELL Stability and Functions.. *Molecular and cellular biology*. PMID: 36036574
5. Stratification and therapeutic potential of ELL in cytogenetic normal acute myeloid leukemia.. *Gene*. PMID: 36543308

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 31.4% |
| 置信残基 (pLDDT 70-90) 占比 | 20.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 38.6% |
| 有序区域 (pLDDT>70) 占比 | 51.9% |
| 可用 PDB 条目 | 2DOA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 51.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042065, IPR031176, IPR019464, IPR010844, IPR036390; Pfam: PF10390, PF07303 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EAF1 | 0.999 | 0.850 | — |
| AFF1 | 0.999 | 0.091 | — |
| MLLT3 | 0.999 | 0.748 | — |
| AFF4 | 0.999 | 0.849 | — |
| MLLT1 | 0.999 | 0.685 | — |
| EAF2 | 0.998 | 0.648 | — |
| CCNT1 | 0.998 | 0.328 | — |
| CDK9 | 0.997 | 0.537 | — |
| ELL3 | 0.992 | 0.833 | — |
| ICE2 | 0.981 | 0.328 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ICE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| ICE2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| USPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Jarid2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| Mtf2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| ELL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| MED26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| EAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| DYRK1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| CDC7 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 2DOA | pLDDT=67.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Nucleus, Cajal body / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 一致 |
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
1. ELL — RNA polymerase II elongation factor ELL，研究基础较多，新颖性有限。
2. 蛋白大小621 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 254 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 254 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55199
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105656-ELL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55199
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000105656-ELL/subcellular

![](https://images.proteinatlas.org/4202/1924_G3_3_red_green.jpg)
![](https://images.proteinatlas.org/4202/1924_G3_4_red_green.jpg)
![](https://images.proteinatlas.org/4202/1947_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/4202/1947_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/4202/1954_F2_45_cr5dfc942b00328_red_green.jpg)
![](https://images.proteinatlas.org/4202/1954_F2_59_cr5dfc942b009bc_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P55199-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
