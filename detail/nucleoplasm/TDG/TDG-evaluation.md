---
type: protein-evaluation
gene: "TDG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TDG — REJECTED (研究热度过高 (PubMed strict=310，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TDG |
| 蛋白名称 | G/T mismatch-specific thymine DNA glycosylase |
| 蛋白大小 | 410 aa / 46.1 kDa |
| UniProt ID | Q13569 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 410 aa / 46.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=310 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=70.2; PDB: 1WYW, 2D07, 2RBA, 3UFJ, 3UO7, 3UOB, 4FNC |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015637, IPR003310, IPR005122, IPR036895; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 310 |
| PubMed broad count | 1046 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mechanism of cytarabine-induced neurotoxicity.. *Nature*. PMID: 40562930
2. 5-Hydroxymethylcytosine and disease.. *Mutation research. Reviews in mutation research*. PMID: 25475423
3. Long-term voluntary exercise inhibited AGE/RAGE and microglial activation and reduced the loss of dendritic spines in the hippocampi of APP/PS1 transgenic mice.. *Experimental neurology*. PMID: 36871860
4. TET1 and TDG Suppress Inflammatory Response in Intestinal Tumorigenesis: Implications for Colorectal Tumors With the CpG Island Methylator Phenotype.. *Gastroenterology*. PMID: 36764492
5. Thymine DNA glycosylase.. *Progress in nucleic acid research and molecular biology*. PMID: 11554300

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.2 |
| 高置信度残基 (pLDDT>90) 占比 | 48.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 42.2% |
| 有序区域 (pLDDT>70) 占比 | 54.4% |
| 可用 PDB 条目 | 1WYW, 2D07, 2RBA, 3UFJ, 3UO7, 3UOB, 4FNC, 4JGC, 4XEG, 4Z3A |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1WYW, 2D07, 2RBA, 3UFJ, 3UO7, 3UOB, 4FNC, 4JGC, 4XEG, 4Z3A）+ AlphaFold极高置信度预测（pLDDT=70.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015637, IPR003310, IPR005122, IPR036895; Pfam: PF03167 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUMO1 | 0.998 | 0.983 | — |
| SUMO2 | 0.994 | 0.970 | — |
| GADD45A | 0.987 | 0.301 | — |
| DNMT3A | 0.933 | 0.292 | — |
| SMUG1 | 0.922 | 0.000 | — |
| UBE2I | 0.910 | 0.630 | — |
| UNG | 0.907 | 0.000 | — |
| APEX1 | 0.905 | 0.000 | — |
| DNMT3B | 0.905 | 0.292 | — |
| MBD4 | 0.902 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Mst98Ca | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| dally | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| DDX39B | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| JUNB | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| IKZF1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| AICDA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21722948|imex:IM-16563 |
| ENSMUSP00000121000.2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:21722948|imex:IM-16563 |
| EBI-4320504 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:21722948|imex:IM-16563 |
| GADD45A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21722948|imex:IM-16563 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.2 + PDB: 1WYW, 2D07, 2RBA, 3UFJ, 3UO7,  | pLDDT=70.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. TDG — G/T mismatch-specific thymine DNA glycosylase，研究基础较多，新颖性有限。
2. 蛋白大小410 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 310 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 310 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13569
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139372-TDG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TDG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13569
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
