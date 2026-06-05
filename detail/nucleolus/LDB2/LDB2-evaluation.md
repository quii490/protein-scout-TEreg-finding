---
type: protein-evaluation
gene: "LDB2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LDB2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LDB2 / CLIM1 |
| 蛋白名称 | LIM domain-binding protein 2 |
| 蛋白大小 | 373 aa / 42.8 kDa |
| UniProt ID | O43679 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; 额外: Plasma membrane; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 42.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR041363, IPR029005; Pfam: PF17916, PF01803 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Plasma membrane | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell leading edge (GO:0031252)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 123 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CLIM1 |

**关键文献**:
1. LDB2 is a novel diagnostic and prognostic biomarker and inhibits bladder cancer metastasis by activating p38 MAPK/ERK1/2/JNK signaling pathway.. *Clinical and experimental medicine*. PMID: 41249576
2. Molecular characterization and a duplicated 31-bp indel within the LDB2 gene and its associations with production performance in chickens.. *Gene*. PMID: 32781192
3. LDB2 regulates the expression of DLL4 through the formation of oligomeric complexes in endothelial cells.. *BMB reports*. PMID: 28946938
4. Cooperation of LIM domain-binding 2 (LDB2) with EGR in the pathogenesis of schizophrenia.. *EMBO molecular medicine*. PMID: 33656268
5. [LIM-domain binding protein 2 regulated by m(6)A modification inhibits lung adenocarcinoma cell proliferation in vitro].. *Nan fang yi ke da xue xue bao = Journal of Southern Medical University*. PMID: 33849822

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.7 |
| 高置信度残基 (pLDDT>90) 占比 | 40.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 31.6% |
| 有序区域 (pLDDT>70) 占比 | 58.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.7，有序区 58.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041363, IPR029005; Pfam: PF17916, PF01803 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMO2 | 0.998 | 0.166 | — |
| GATA1 | 0.995 | 0.127 | — |
| TAL1 | 0.995 | 0.087 | — |
| TCF3 | 0.992 | 0.045 | — |
| GATA2 | 0.983 | 0.113 | — |
| CBFA2T3 | 0.981 | 0.046 | — |
| LYL1 | 0.966 | 0.074 | — |
| ISL1 | 0.965 | 0.399 | — |
| LMO1 | 0.955 | 0.456 | — |
| LHX2 | 0.941 | 0.399 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000306772.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SMARCD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PSMB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SDCBP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EXOC3L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EPM2AIP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| C14orf119 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MYDGF | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.7 + PDB: 无 | pLDDT=72.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli; 额外: Plasma membrane | 一致 |
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
1. LDB2 — LIM domain-binding protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43679
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169744-LDB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LDB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43679
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000169744-LDB2/subcellular

![](https://images.proteinatlas.org/68634/1332_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/68634/1332_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/68634/1358_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/68634/1358_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/68634/1593_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/68634/1593_F2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43679-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
