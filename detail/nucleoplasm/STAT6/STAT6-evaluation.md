---
type: protein-evaluation
gene: "STAT6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STAT6 — REJECTED (研究热度过高 (PubMed strict=2409，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAT6 |
| 蛋白名称 | Signal transducer and activator of transcription 6 |
| 蛋白大小 | 847 aa / 94.1 kDa |
| UniProt ID | P42226 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Connecting piece; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 847 aa / 94.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2409 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.5; PDB: 1OJ5, 4Y5U, 4Y5W, 5D39, 5NWM, 5NWX, 9BIG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR028 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Connecting piece | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)
- sperm head-tail coupling apparatus (GO:0120212)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2409 |
| PubMed broad count | 5123 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. STAT6/Arg1 promotes microglia/macrophage efferocytosis and inflammation resolution in stroke mice.. *JCI insight*. PMID: 31619589
2. Human germline heterozygous gain-of-function STAT6 variants cause severe allergic disease.. *The Journal of experimental medicine*. PMID: 36884218
3. Follicular lymphoma t(14;18)-negative is genetically a heterogeneous disease.. *Blood advances*. PMID: 33211828
4. Discovery of AK-1690: A Potent and Highly Selective STAT6 PROTAC Degrader.. *Journal of medicinal chemistry*. PMID: 39311434
5. STAT6 inhibits ferroptosis and alleviates acute lung injury via regulating P53/SLC7A11 pathway.. *Cell death & disease*. PMID: 35668064

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.5 |
| 高置信度残基 (pLDDT>90) 占比 | 53.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 24.1% |
| 有序区域 (pLDDT>70) 占比 | 71.4% |
| 可用 PDB 条目 | 1OJ5, 4Y5U, 4Y5W, 5D39, 5NWM, 5NWX, 9BIG |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1OJ5, 4Y5U, 4Y5W, 5D39, 5NWM, 5NWX, 9BIG）+ AlphaFold极高置信度预测（pLDDT=76.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR028187; Pfam: PF00017, PF14596, PF01017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IL4R | 0.999 | 0.757 | — |
| NCOA1 | 0.997 | 0.983 | — |
| IL4 | 0.997 | 0.000 | — |
| JAK1 | 0.996 | 0.472 | — |
| STAT2 | 0.991 | 0.292 | — |
| JAK2 | 0.991 | 0.285 | — |
| JAK3 | 0.990 | 0.472 | — |
| IRF9 | 0.987 | 0.112 | — |
| IRF4 | 0.975 | 0.510 | — |
| IL13 | 0.971 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000519640.1 | psi-mi:"MI:0404"(comigration in non denaturing gel | pubmed:22000020|imex:IM-16625 |
| Gpi | psi-mi:"MI:0018"(two hybrid) | pubmed:17875708|imex:IM-19750 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.5 + PDB: 1OJ5, 4Y5U, 4Y5W, 5D39, 5NWM,  | pLDDT=76.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol; 额外: Connecting piece | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. STAT6 — Signal transducer and activator of transcription 6，研究基础较多，新颖性有限。
2. 蛋白大小847 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2409 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2409 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P42226
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166888-STAT6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAT6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P42226
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
