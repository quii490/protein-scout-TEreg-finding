---
type: protein-evaluation
gene: "SP140"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SP140 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SP140 / LYSP100 |
| 蛋白名称 | Nuclear body protein SP140 |
| 蛋白大小 | 867 aa / 98.2 kDa |
| UniProt ID | Q13342 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; 额外: Mitochondria; UniProt: Nucleus; Nucleus, PML body; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 867 aa / 98.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=69 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.0; PDB: 2MD7, 2MD8, 6G8R, 8J70, 8J71 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001487, IPR036427, IPR004865, IPR010919, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Mitochondria | Approved |
| UniProt | Nucleus; Nucleus, PML body; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- fibrillar center (GO:0001650)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 69 |
| PubMed broad count | 96 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LYSP100 |

**关键文献**:
1. SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity.. *Nature*. PMID: 40500448
2. Epigenetic reader SP140 loss of function drives Crohn's disease due to uncontrolled macrophage topoisomerases.. *Cell*. PMID: 35952671
3. Transcriptional regulators SP110 and SP140 modulate inflammatory response genes in Mycobacterium tuberculosis-infected human macrophages.. *Microbiology spectrum*. PMID: 39162523
4. Transient SP140 inhibition unlocks hematopoietic stem cell fate from human pluripotent stem cells.. *Blood*. PMID: 41397285
5. Role of the transcriptional regulator SP140 in resistance to bacterial infections via repression of type I interferons.. *eLife*. PMID: 34151776

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.0 |
| 高置信度残基 (pLDDT>90) 占比 | 18.8% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 57.3% |
| 有序区域 (pLDDT>70) 占比 | 37.8% |
| 可用 PDB 条目 | 2MD7, 2MD8, 6G8R, 8J70, 8J71 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.0），有序残基占 37.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001487, IPR036427, IPR004865, IPR010919, IPR000770; Pfam: PF00439, PF03172, PF00628 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SP140L | 0.903 | 0.800 | — |
| IGKV1-33 | 0.900 | 0.900 | — |
| IGKV1D-33 | 0.900 | 0.900 | — |
| AIM2 | 0.689 | 0.000 | — |
| PPIE | 0.638 | 0.000 | — |
| TENT5C | 0.592 | 0.000 | — |
| PML | 0.575 | 0.000 | — |
| ISG20 | 0.563 | 0.000 | — |
| DIS3 | 0.540 | 0.000 | — |
| CBX5 | 0.539 | 0.065 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ilvI | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| pnp | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ERP29 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| NFE2L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32911434|imex:IM-27648 |
| ZMYND11 | psi-mi:"MI:0084"(phage display) | imex:IM-29361|pubmed:35044719 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.0 + PDB: 2MD7, 2MD8, 6G8R, 8J70, 8J71 | pLDDT=57.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, PML body; Cytoplasm / Nucleoli fibrillar center; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SP140 — Nuclear body protein SP140，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小867 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 69 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13342
- Protein Atlas: https://www.proteinatlas.org/ENSG00000079263-SP140/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SP140
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13342
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
