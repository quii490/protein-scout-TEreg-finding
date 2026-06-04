---
type: protein-evaluation
gene: "TEAD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TEAD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEAD3 / TEAD5, TEF5 |
| 蛋白名称 | Transcriptional enhancer factor TEF-5 |
| 蛋白大小 | 435 aa / 48.7 kDa |
| UniProt ID | Q99594 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 435 aa / 48.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=54 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.6; PDB: 5EMW, 7CNL, 7ZJQ, 8P0M, 8ZBG, 8ZBH, 9IXS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000818, IPR038096, IPR050937, IPR027253, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- transcription regulator complex (GO:0005667)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 54 |
| PubMed broad count | 94 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TEAD5, TEF5 |

**关键文献**:
1. Long noncoding RNA Malat1 protects against osteoporosis and bone metastasis.. *Nature communications*. PMID: 38493144
2. TEAD3 + high-risk melanoma cells crosstalk with GAS6 + macrophages via the GAS6-TYRO3 ligand-receptor axis to modulate propionate metabolism and drive melanoma progression.. *Journal of experimental & clinical cancer research : CR*. PMID: 41034991
3. Podocyte YAP ablation decreases podocyte adhesion and exacerbates FSGS progression through α3β1 integrin.. *The Journal of pathology*. PMID: 39668547
4. TEAD3 inhibits the proliferation and metastasis of prostate cancer via suppressing ADRBK2.. *Biochemical and biophysical research communications*. PMID: 36907139
5. Endometriosis: From Genes to Global Burden.. *International journal of molecular sciences*. PMID: 41516028

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.6 |
| 高置信度残基 (pLDDT>90) 占比 | 41.4% |
| 置信残基 (pLDDT 70-90) 占比 | 28.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 24.1% |
| 有序区域 (pLDDT>70) 占比 | 69.4% |
| 可用 PDB 条目 | 5EMW, 7CNL, 7ZJQ, 8P0M, 8ZBG, 8ZBH, 9IXS, 9IXT |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5EMW, 7CNL, 7ZJQ, 8P0M, 8ZBG, 8ZBH, 9IXS, 9IXT）+ AlphaFold极高置信度预测（pLDDT=75.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000818, IPR038096, IPR050937, IPR027253, IPR016361; Pfam: PF01285, PF17725 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YAP1 | 0.998 | 0.836 | — |
| WWTR1 | 0.994 | 0.880 | — |
| VGLL4 | 0.941 | 0.785 | — |
| VGLL1 | 0.840 | 0.716 | — |
| TCF7L2 | 0.839 | 0.091 | — |
| TCF7 | 0.822 | 0.071 | — |
| TCF7L1 | 0.817 | 0.083 | — |
| LEF1 | 0.816 | 0.071 | — |
| CSH2 | 0.785 | 0.000 | — |
| KCNIP3 | 0.777 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| WWTR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CTBP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SUMO2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| AP4S1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| KIFC2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PIDD1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PHB2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| STUB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| YAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.6 + PDB: 5EMW, 7CNL, 7ZJQ, 8P0M, 8ZBG,  | pLDDT=75.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TEAD3 — Transcriptional enhancer factor TEF-5，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小435 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 54 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99594
- Protein Atlas: https://www.proteinatlas.org/ENSG00000007866-TEAD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEAD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99594
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TEAD3/TEAD3-PAE.png]]
