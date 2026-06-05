---
type: protein-evaluation
gene: "MESP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MESP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MESP2 / BHLHC6, SCDO2 |
| 蛋白名称 | Mesoderm posterior protein 2 |
| 蛋白大小 | 397 aa / 41.8 kDa |
| UniProt ID | Q0VG99 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 397 aa / 41.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=64 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR040259; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

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
| PubMed strict count | 64 |
| PubMed broad count | 136 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHC6, SCDO2 |

**关键文献**:
1. Reconstruction and deconstruction of human somitogenesis in vitro.. *Nature*. PMID: 36543321
2. Retinoic acid enhances ovarian steroidogenesis by regulating granulosa cell proliferation and MESP2/STAR/CYP11A1 pathway.. *Journal of advanced research*. PMID: 37315842
3. Spondylocostal Dysostosis, Autosomal Recessive.. **. PMID: 20301771
4. Mesp2: a novel mouse gene expressed in the presegmented mesoderm and essential for segmentation initiation.. *Genes & development*. PMID: 9242490
5. Mutation analysis of MESP2, HES7 and DUSP6 gene exons in patients with congenital scoliosis.. *Studies in health technology and informatics*. PMID: 22744456

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.2 |
| 高置信度残基 (pLDDT>90) 占比 | 11.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 23.4% |
| 低置信 (pLDDT<50) 占比 | 58.4% |
| 有序区域 (pLDDT>70) 占比 | 18.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.2），有序残基占 18.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR040259; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBX6 | 0.979 | 0.065 | — |
| LFNG | 0.925 | 0.000 | — |
| DLL3 | 0.857 | 0.045 | — |
| TCF4 | 0.822 | 0.811 | — |
| TCF3 | 0.820 | 0.808 | — |
| RIPPLY2 | 0.807 | 0.000 | — |
| TCF12 | 0.805 | 0.792 | — |
| DLL1 | 0.777 | 0.045 | — |
| RIPPLY1 | 0.697 | 0.000 | — |
| TBX18 | 0.694 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TCF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCF12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TUSC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACSL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| USP34 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SLC25A15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.2 + PDB: 无 | pLDDT=54.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MESP2 — Mesoderm posterior protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小397 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 64 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q0VG99
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188095-MESP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MESP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q0VG99
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q0VG99-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
