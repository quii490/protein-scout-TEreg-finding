---
type: protein-evaluation
gene: "CTBP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTBP1 — REJECTED (研究热度过高 (PubMed strict=341，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTBP1 / CTBP |
| 蛋白名称 | C-terminal-binding protein 1 |
| 蛋白大小 | 440 aa / 47.5 kDa |
| UniProt ID | Q13363 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 440 aa / 47.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=341 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=83.3; PDB: 1MX3, 4LCE, 4U6Q, 4U6S, 6CDF, 6CDR, 6V89 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR043322, IPR051638, IPR006139, IPR029753, IPR029 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- GABA-ergic synapse (GO:0098982)
- glutamatergic synapse (GO:0098978)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- presynaptic active zone cytoplasmic component (GO:0098831)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 341 |
| PubMed broad count | 425 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CTBP |

**关键文献**:
1. Wolf-Hirschhorn Syndrome – RETIRED CHAPTER, FOR HISTORICAL REFERENCE ONLY.. **. PMID: 20301362
2. The evolving epigenome.. *Human molecular genetics*. PMID: 23900077
3. CTBP1 links metabolic syndrome to polycystic ovary syndrome through interruption of aromatase and SREBP1.. *Communications biology*. PMID: 39294274
4. CtBP1/2 oligomerization promotes G9a-Mediated transcriptional repression.. *The Journal of biological chemistry*. PMID: 41419197
5. Endothelial nucleotide-binding oligomerization domain-like receptor protein 3 inflammasome regulation in atherosclerosis.. *Cardiovascular research*. PMID: 38626254

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.3 |
| 高置信度残基 (pLDDT>90) 占比 | 73.9% |
| 置信残基 (pLDDT 70-90) 占比 | 1.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 22.5% |
| 有序区域 (pLDDT>70) 占比 | 75.3% |
| 可用 PDB 条目 | 1MX3, 4LCE, 4U6Q, 4U6S, 6CDF, 6CDR, 6V89, 6V8A, 7KWM, 8ARI |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=83.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043322, IPR051638, IPR006139, IPR029753, IPR029752; Pfam: PF00389, PF02826 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTBP2 | 0.999 | 0.895 | — |
| RCOR1 | 0.999 | 0.820 | — |
| HDAC2 | 0.999 | 0.811 | — |
| HDAC1 | 0.999 | 0.837 | — |
| RBBP8 | 0.998 | 0.815 | — |
| KDM1A | 0.998 | 0.850 | — |
| ZEB1 | 0.998 | 0.848 | — |
| ZNF217 | 0.997 | 0.877 | — |
| MECOM | 0.994 | 0.726 | — |
| KLF3 | 0.990 | 0.265 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.3 + PDB: 1MX3, 4LCE, 4U6Q, 4U6S, 6CDF,  | pLDDT=83.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CTBP1 -- C-terminal-binding protein 1，研究基础较多，新颖性有限。
2. 蛋白大小440 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 341 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 341 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13363
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159692-CTBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13363
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
