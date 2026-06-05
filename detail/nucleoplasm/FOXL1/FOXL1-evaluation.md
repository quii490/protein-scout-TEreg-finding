---
type: protein-evaluation
gene: "FOXL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXL1 — REJECTED (研究热度过高 (PubMed strict=117，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXL1 / FKHL11, FREAC7 |
| 蛋白名称 | Forkhead box protein L1 |
| 蛋白大小 | 345 aa / 36.5 kDa |
| UniProt ID | Q12952 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 345 aa / 36.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=117 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047514, IPR001766, IPR050211, IPR018122, IPR030 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 117 |
| PubMed broad count | 179 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKHL11, FREAC7 |

**关键文献**:
1. The Balance of Stromal BMP Signaling Mediated by GREM1 and ISLR Drives Colorectal Carcinogenesis.. *Gastroenterology*. PMID: 33197448
2. FHL5 Controls Vascular Disease-Associated Gene Programs in Smooth Muscle Cells.. *Circulation research*. PMID: 37017084
3. Human FOX gene family (Review).. *International journal of oncology*. PMID: 15492844
4. FOXL1+ Telocytes in mouse colon orchestrate extracellular matrix biodynamics and wound repair resolution.. *Journal of proteomics*. PMID: 36272709
5. Cellular origins of regenerating liver and hepatocellular carcinoma.. *JHEP reports : innovation in hepatology*. PMID: 35243280

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 21.2% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 31.6% |
| 低置信 (pLDDT<50) 占比 | 38.0% |
| 有序区域 (pLDDT>70) 占比 | 30.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 30.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047514, IPR001766, IPR050211, IPR018122, IPR030456; Pfam: PF00250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GLI1 | 0.742 | 0.096 | — |
| CPS1 | 0.729 | 0.000 | — |
| GLI2 | 0.696 | 0.096 | — |
| GLI3 | 0.673 | 0.096 | — |
| MTHFSD | 0.637 | 0.000 | — |
| SHH | 0.589 | 0.000 | — |
| SLC5A1 | 0.578 | 0.000 | — |
| FOXC2 | 0.563 | 0.103 | — |
| CTNNB1 | 0.548 | 0.071 | — |
| AIMP1 | 0.543 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BMPR2 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Hsl | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Scot | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dph1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG11771 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Tango6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| NUCB1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Vha100-2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| YL-1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| wdb | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 无 | pLDDT=62.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOXL1 — Forkhead box protein L1，研究基础较多，新颖性有限。
2. 蛋白大小345 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 117 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 117 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12952
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176678-FOXL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12952
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12952-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
