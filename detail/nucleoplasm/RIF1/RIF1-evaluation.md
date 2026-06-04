---
type: protein-evaluation
gene: "RIF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RIF1 — REJECTED (研究热度过高 (PubMed strict=299，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RIF1 |
| 蛋白名称 | Telomere-associated protein RIF1 |
| 蛋白大小 | 2472 aa / 274.5 kDa |
| UniProt ID | Q5UIP0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear membrane, Plasma membrane; UniProt: Nucleus; Chromosome; Chromosome, telomere; Cytoplasm, cytosk |
| 蛋白大小 | 2/10 | ×1 | 2 | 2472 aa / 274.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=299 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.8; PDB: 8RS8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR022031; Pfam: PF12231 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **72.5/180** | |
| **归一化总分** | | | **40.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear membrane, Plasma membrane | Supported |
| UniProt | Nucleus; Chromosome; Chromosome, telomere; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, telomeric repeat region (GO:0140445)
- condensed chromosome (GO:0000793)
- female pronucleus (GO:0001939)
- male pronucleus (GO:0001940)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 299 |
| PubMed broad count | 948 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The shieldin complex mediates 53BP1-dependent DNA repair.. *Nature*. PMID: 30022168
2. Comparison of Telomere Structure in Eukaryotes.. *Archives of Razi Institute*. PMID: 40606259
3. Longitudinal profiling identifies co-occurring BRCA1/2 reversions, TP53BP1, RIF1 and PAXIP1 mutations in PARP inhibitor-resistant advanced breast cancer.. *Annals of oncology : official journal of the European Society for Medical Oncology*. PMID: 38244928
4. 53BP1-RIF1-shieldin counteracts DSB resection through CST- and Polα-dependent fill-in.. *Nature*. PMID: 30022158
5. Ceramide-induced cleavage of GPR64 intracellular domain drives Ewing sarcoma.. *Cell reports*. PMID: 39024100

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.8 |
| 高置信度残基 (pLDDT>90) 占比 | 18.0% |
| 置信残基 (pLDDT 70-90) 占比 | 21.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 57.9% |
| 有序区域 (pLDDT>70) 占比 | 39.3% |
| 可用 PDB 条目 | 8RS8 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.8），有序残基占 39.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR022031; Pfam: PF12231 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TP53BP1 | 0.953 | 0.638 | — |
| PAXIP1 | 0.938 | 0.052 | — |
| PPP1CA | 0.834 | 0.810 | — |
| ATM | 0.823 | 0.054 | — |
| PPP1CC | 0.816 | 0.794 | — |
| BRCA1 | 0.813 | 0.439 | — |
| MDC1 | 0.795 | 0.445 | — |
| BLM | 0.782 | 0.620 | — |
| H4C6 | 0.780 | 0.525 | — |
| PIAS4 | 0.742 | 0.314 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| P89507 | psi-mi:"MI:0067"(light scattering) | imex:IM-21427|pubmed:23746845 |
| NOC2L | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GPRASP2 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| GIT1 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| LRIF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| BARD1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| GADD45G | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| Hap1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| KAT7 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| IMMT | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.8 + PDB: 8RS8 | pLDDT=53.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Chromosome, telomere; Cytopla / Nucleoplasm; 额外: Nuclear membrane, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RIF1 — Telomere-associated protein RIF1，研究基础较多，新颖性有限。
2. 蛋白大小2472 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 299 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 299 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5UIP0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000080345-RIF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RIF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5UIP0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
