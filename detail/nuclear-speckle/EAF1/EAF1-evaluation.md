---
type: protein-evaluation
gene: "EAF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EAF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EAF1 |
| 蛋白名称 | ELL-associated factor 1 |
| 蛋白大小 | 268 aa / 29.0 kDa |
| UniProt ID | Q96JC9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear bodies; 额外: Vesicles; UniProt: Nucleus speckle; Nucleus, Cajal body |
| 蛋白大小 | 10/10 | ×1 | 10 | 268 aa / 29.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=70.7; PDB: 7OKX, 7OKY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027093, IPR019194; Pfam: PF09816 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Vesicles | Approved |
| UniProt | Nucleus speckle; Nucleus, Cajal body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cajal body (GO:0015030)
- intercellular bridge (GO:0045171)
- nuclear body (GO:0016604)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- super elongation complex (GO:0032783)
- transcription elongation factor complex (GO:0008023)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 83 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Negative Feedback Loop Mechanism between EAF1/2 and DBC1 in Regulating ELL Stability and Functions.. *Molecular and cellular biology*. PMID: 36036574
2. HBO1-MLL interaction promotes AF4/ENL/P-TEFb-mediated leukemogenesis.. *eLife*. PMID: 34431785
3. Architecture of the Saccharomyces cerevisiae NuA4/TIP60 complex.. *Nature communications*. PMID: 29559617
4. Transcriptional factors Eaf1/2 inhibit endoderm and mesoderm formation via suppressing TGF-β signaling.. *Biochimica et biophysica acta. Gene regulatory mechanisms*. PMID: 28887217
5. Lactylation-related gene signatures define immune heterogeneity and provide diagnostic biomarkers for periodontitis.. *Scientific reports*. PMID: 41310117

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.7 |
| 高置信度残基 (pLDDT>90) 占比 | 31.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 29.9% |
| 低置信 (pLDDT<50) 占比 | 20.9% |
| 有序区域 (pLDDT>70) 占比 | 49.2% |
| 可用 PDB 条目 | 7OKX, 7OKY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7OKX, 7OKY）+ AlphaFold高质量预测（pLDDT=70.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027093, IPR019194; Pfam: PF09816 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELL2 | 0.999 | 0.873 | — |
| ELL | 0.999 | 0.850 | — |
| AFF1 | 0.997 | 0.812 | — |
| ELL3 | 0.992 | 0.848 | — |
| AFF4 | 0.992 | 0.788 | — |
| MLLT3 | 0.991 | 0.767 | — |
| MLLT1 | 0.990 | 0.721 | — |
| ICE1 | 0.982 | 0.781 | — |
| EAF2 | 0.982 | 0.810 | — |
| ICE2 | 0.974 | 0.525 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EAF7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15353583 |
| EAF6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15353583 |
| EAF5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15353583 |
| YNG2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15353583 |
| EPL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15353583 |
| ESA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15353583 |
| ADA2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| EAF3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ACT1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| ABF2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.7 + PDB: 7OKX, 7OKY | pLDDT=70.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus speckle; Nucleus, Cajal body / Nucleoplasm, Nuclear bodies; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EAF1 — ELL-associated factor 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小268 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96JC9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144597-EAF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EAF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JC9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000144597-EAF1/subcellular

![](https://images.proteinatlas.org/59516/1070_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/59516/1070_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/59516/1076_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/59516/1076_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/59516/1259_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/59516/1259_B7_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96JC9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
