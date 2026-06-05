---
type: protein-evaluation
gene: "BMAL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BMAL1 — REJECTED (研究热度过高 (PubMed strict=2678，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BMAL1 / ARNTL, BHLHE5, MOP3, PASD3 |
| 蛋白名称 | Basic helix-loop-helix ARNT-like protein 1 |
| 蛋白大小 | 626 aa / 68.8 kDa |
| UniProt ID | O00327 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus; Cytoplasm; Nucleus, PML body |
| 蛋白大小 | 10/10 | ×1 | 10 | 626 aa / 68.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2678 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.5; PDB: 4H10, 8RW6, 8RW8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050933, IPR036638, IPR001067, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus; Cytoplasm; Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- aryl hydrocarbon receptor complex (GO:0034751)
- chromatin (GO:0000785)
- chromatoid body (GO:0033391)
- CLOCK-BMAL transcription complex (GO:1990513)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2678 |
| PubMed broad count | 3890 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARNTL, BHLHE5, MOP3, PASD3 |

**关键文献**:
1. Bmal1 downregulation leads to diabetic cardiomyopathy by promoting Bcl2/IP3R-mediated mitochondrial Ca(2+) overload.. *Redox biology*. PMID: 37356134
2. Deficiency of intestinal Bmal1 prevents obesity induced by high-fat feeding.. *Nature communications*. PMID: 34493722
3. An astrocyte BMAL1-BAG3 axis protects against alpha-synuclein and tau pathology.. *Neuron*. PMID: 37315555
4. Pharmacological targeting of BMAL1 modulates circadian and immune pathways.. *Nature chemical biology*. PMID: 40133642
5. Endothelial BMAL1 decline during aging leads to bone loss by destabilizing extracellular fibrillin-1.. *The Journal of clinical investigation*. PMID: 39680455

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.5 |
| 高置信度残基 (pLDDT>90) 占比 | 33.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.8% |
| 低置信 (pLDDT<50) 占比 | 40.4% |
| 有序区域 (pLDDT>70) 占比 | 46.8% |
| 可用 PDB 条目 | 4H10, 8RW6, 8RW8 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.5），有序残基占 46.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050933, IPR036638, IPR001067, IPR001610; Pfam: PF00010, PF00989, PF14598 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRY1 | 0.999 | 0.982 | — |
| NPAS2 | 0.999 | 0.919 | — |
| CLOCK | 0.999 | 0.994 | — |
| CRY2 | 0.999 | 0.973 | — |
| PER2 | 0.997 | 0.963 | — |
| SIRT1 | 0.997 | 0.345 | — |
| CSNK1E | 0.997 | 0.696 | — |
| NPAS4 | 0.990 | 0.585 | — |
| BHLHE41 | 0.989 | 0.089 | — |
| NR1D1 | 0.989 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sirt1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11902|pubmed:18662546 |
| Clock | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11902|pubmed:18662546 |
| Hlf | psi-mi:"MI:0018"(two hybrid) | pubmed:9704006|imex:IM-20272 |
| HIF1A | psi-mi:"MI:0018"(two hybrid) | pubmed:9704006|imex:IM-20272 |
| EPAS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11018023|imex:IM-20044 |
| Per2 | psi-mi:"MI:0728"(gal4 vp16 complementation) | pubmed:18430226|imex:IM-18930 |
| Cry1 | psi-mi:"MI:0728"(gal4 vp16 complementation) | pubmed:18430226|imex:IM-18930 |
| Cry2 | psi-mi:"MI:0728"(gal4 vp16 complementation) | pubmed:18430226|imex:IM-18930 |
| Parp1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:20832105|imex:IM-15197 |
| Q9WTL9 | psi-mi:"MI:0412"(electrophoretic mobility supershi | pubmed:20832105|imex:IM-15197 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.5 + PDB: 4H10, 8RW6, 8RW8 | pLDDT=65.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus, PML body / Nucleoplasm; 额外: Vesicles | 一致 |
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
1. BMAL1 — Basic helix-loop-helix ARNT-like protein 1，研究基础较多，新颖性有限。
2. 蛋白大小626 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2678 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2678 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00327
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133794-BMAL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BMAL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00327
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000133794-BMAL1/subcellular

![](https://images.proteinatlas.org/50938/827_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/50938/827_F10_4_red_green.jpg)
![](https://images.proteinatlas.org/50938/829_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/50938/829_F10_4_red_green.jpg)
![](https://images.proteinatlas.org/50938/977_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/50938/977_F10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
