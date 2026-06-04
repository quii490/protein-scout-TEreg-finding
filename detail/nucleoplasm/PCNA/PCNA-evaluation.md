---
type: protein-evaluation
gene: "PCNA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PCNA — REJECTED (研究热度过高 (PubMed strict=9353，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCNA |
| 蛋白名称 | DNA sliding clamp PCNA |
| 蛋白大小 | 261 aa / 28.8 kDa |
| UniProt ID | P12004 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 261 aa / 28.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=9353 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.3; PDB: 1AXC, 1U76, 1U7B, 1UL1, 1VYJ, 1VYM, 1W60 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR046938, IPR000730, IPR022649, IPR022659, IPR022 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromatin (GO:0000785)
- chromosome, telomeric region (GO:0000781)
- cyclin-dependent protein kinase holoenzyme complex (GO:0000307)
- extracellular exosome (GO:0070062)
- male germ cell nucleus (GO:0001673)
- nuclear body (GO:0016604)
- nuclear lamina (GO:0005652)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9353 |
| PubMed broad count | 19782 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Human PCNA Structure, Function and Interactions.. *Biomolecules*. PMID: 32276417
2. PCNA: structure, functions and interactions.. *Oncogene*. PMID: 9038370
3. Protein-PCNA interactions: a DNA-scanning mechanism?. *Trends in biochemical sciences*. PMID: 9697409
4. Maneuvers on PCNA Rings during DNA Replication and Repair.. *Genes*. PMID: 30126151
5. Targeting proliferating cell nuclear antigen (PCNA) for cancer therapy.. *Advances in pharmacology (San Diego, Calif.)*. PMID: 39034053

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.3 |
| 高置信度残基 (pLDDT>90) 占比 | 88.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 1.5% |
| 有序区域 (pLDDT>70) 占比 | 97.7% |
| 可用 PDB 条目 | 1AXC, 1U76, 1U7B, 1UL1, 1VYJ, 1VYM, 1W60, 2ZVK, 2ZVL, 2ZVM |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1AXC, 1U76, 1U7B, 1UL1, 1VYJ, 1VYM, 1W60, 2ZVK, 2ZVL, 2ZVM）+ AlphaFold极高置信度预测（pLDDT=94.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046938, IPR000730, IPR022649, IPR022659, IPR022648; Pfam: PF02747, PF00705 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POLH | 0.999 | 0.997 | — |
| POLD1 | 0.999 | 0.993 | — |
| FEN1 | 0.999 | 0.999 | — |
| CDKN1A | 0.999 | 0.999 | — |
| RFC3 | 0.999 | 0.997 | — |
| RFC2 | 0.999 | 0.997 | — |
| RFC4 | 0.999 | 0.997 | — |
| LIG1 | 0.999 | 0.997 | — |
| RFC5 | 0.999 | 0.997 | — |
| RFC1 | 0.999 | 0.998 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSCGRP00001027378.1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:15805117|imex:IM-19570 |
| ENSP00000368458.3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:15805117|imex:IM-19570 |
| POL30 | psi-mi:"MI:0071"(molecular sieving) | pubmed:11545742|imex:IM-19917 |
| ENSMUSP00000028817.7 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| pcn-1 | psi-mi:"MI:0018"(two hybrid) | doi:10.1016/j.cell.2012.11.042 |
| EBI-458654 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| RAD27 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:7673186|mint:MINT-52205 |
| RPS20 | psi-mi:"MI:0018"(two hybrid) | pubmed:12684538 |
| Rubq1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12684538 |
| FEN1 | psi-mi:"MI:0055"(fluorescent resonance energy tran | pubmed:14657243 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.3 + PDB: 1AXC, 1U76, 1U7B, 1UL1, 1VYJ,  | pLDDT=94.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. PCNA — DNA sliding clamp PCNA，研究基础较多，新颖性有限。
2. 蛋白大小261 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9353 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 9353 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P12004
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132646-PCNA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCNA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P12004
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
