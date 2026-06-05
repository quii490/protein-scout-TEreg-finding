---
type: protein-evaluation
gene: "CIDEA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CIDEA — REJECTED (研究热度过高 (PubMed strict=403，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIDEA |
| 蛋白名称 | Lipid transferase CIDEA |
| 蛋白大小 | 219 aa / 24.7 kDa |
| UniProt ID | O60543 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Lipid droplet; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 219 aa / 24.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=403 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=75.3; PDB: 2EEL |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003508, IPR032936; Pfam: PF02017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Lipid droplet; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- lipid droplet (GO:0005811)
- mitochondrial envelope (GO:0005740)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 403 |
| PubMed broad count | 671 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Functional analysis of FSP27 protein regions for lipid droplet localization, caspase-dependent apoptosis, and dimerization with CIDEA.. *American journal of physiology. Endocrinology and metabolism*. PMID: 19843876
2. Apobec1 complementation factor overexpression promotes hepatic steatosis, fibrosis, and hepatocellular cancer.. *The Journal of clinical investigation*. PMID: 33445170
3. Cidea Targeting Protects Cochlear Hair Cells and Hearing Function From Drug- and Noise-Induced Damage.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 41262044
4. Spatial multi-omics characterizes GPR35-relevant lipid metabolism signatures across liver zonation in MASLD.. *Life metabolism*. PMID: 39873004
5. Moderate Treadmill Exercise Alleviates NAFLD by Regulating the Biogenesis and Autophagy of Lipid Droplet.. *Nutrients*. PMID: 36432597

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 31.1% |
| 置信残基 (pLDDT 70-90) 占比 | 38.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 21.0% |
| 有序区域 (pLDDT>70) 占比 | 69.5% |
| 可用 PDB 条目 | 2EEL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=75.3，有序区 69.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003508, IPR032936; Pfam: PF02017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLIN1 | 0.959 | 0.000 | — |
| CIDEC | 0.958 | 0.301 | — |
| UCP1 | 0.956 | 0.000 | — |
| PRDM16 | 0.881 | 0.046 | — |
| DFFB | 0.875 | 0.244 | — |
| LIPE | 0.853 | 0.000 | — |
| ELOVL3 | 0.843 | 0.000 | — |
| PPARG | 0.839 | 0.000 | — |
| COX7A1 | 0.816 | 0.000 | — |
| PPARGC1A | 0.811 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZBTB16 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MIEF2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| IGHG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ICAM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KPRP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SERPINA12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ALB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 2EEL | pLDDT=75.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lipid droplet; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CIDEA — Lipid transferase CIDEA，研究基础较多，新颖性有限。
2. 蛋白大小219 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 403 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 403 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60543
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176194-CIDEA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIDEA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60543
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60543-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
