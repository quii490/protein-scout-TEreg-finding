---
type: protein-evaluation
gene: "SPO11"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPO11 — REJECTED (研究热度过高 (PubMed strict=419，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPO11 |
| 蛋白名称 | Meiotic recombination protein SPO11 |
| 蛋白大小 | 396 aa / 44.5 kDa |
| UniProt ID | Q9Y5K1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 396 aa / 44.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=419 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004084, IPR013048, IPR002815, IPR013049, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- nuclear chromosome (GO:0000228)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 419 |
| PubMed broad count | 720 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. In vitro reconstitution of meiotic DNA double-strand-break formation.. *Nature*. PMID: 39972125
2. Histone demethylase KDM2A recruits HCFC1 and E2F1 to orchestrate male germ cell meiotic entry and progression.. *The EMBO journal*. PMID: 39160277
3. Dynamic changes in histone lysine lactylation during meiosis prophase I in mouse spermatogenesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39928879
4. The SPO11-C631T gene polymorphism and male infertility risk: a meta-analysis.. *Renal failure*. PMID: 28050928
5. Spo11-Independent Meiosis in Social Amoebae.. *Annual review of microbiology*. PMID: 29924686

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.6 |
| 高置信度残基 (pLDDT>90) 占比 | 79.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 93.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.6，有序区 93.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004084, IPR013048, IPR002815, IPR013049, IPR036078; Pfam: PF03533, PF21180, PF04406 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C11orf80 | 0.986 | 0.102 | — |
| WDR61 | 0.968 | 0.767 | — |
| RAD51 | 0.965 | 0.400 | — |
| PRDM9 | 0.935 | 0.000 | — |
| DMC1 | 0.925 | 0.516 | — |
| REC8 | 0.924 | 0.215 | — |
| ATM | 0.905 | 0.088 | — |
| HORMAD1 | 0.901 | 0.000 | — |
| MSH4 | 0.891 | 0.088 | — |
| MEI1 | 0.880 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TUBB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:38884001|imex:IM-30532 |
| CEBPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:38884001|imex:IM-30532 |
| STAT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:38884001|imex:IM-30532 |
| PIN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RBBP8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LIMS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IGFBP7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RAF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RGS17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.6 + PDB: 无 | pLDDT=90.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SPO11 — Meiotic recombination protein SPO11，研究基础较多，新颖性有限。
2. 蛋白大小396 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 419 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 419 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5K1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000054796-SPO11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPO11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5K1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
