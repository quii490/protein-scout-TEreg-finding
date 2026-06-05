---
type: protein-evaluation
gene: "MCTP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MCTP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MCTP2 |
| 蛋白名称 | Multiple C2 and transmembrane domain-containing protein 2 |
| 蛋白大小 | 878 aa / 99.6 kDa |
| UniProt ID | Q6DN12 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 878 aa / 99.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.2; PDB: 2EP6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR013583; Pfam: PF00168, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Enhanced |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- synaptic vesicle membrane (GO:0030672)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Lipid droplet biogenesis.. *Current opinion in cell biology*. PMID: 31075519
2. Genome-wide association study of neuropathological features in Lewy body disease.. *Brain : a journal of neurology*. PMID: 40091616
3. MCTP2 is a novel biomarker promoting tumor progression and nodal metastasis in oral squamous cell carcinoma.. *Scientific reports*. PMID: 40425609
4. MCTP2 is a dosage-sensitive gene required for cardiac outflow tract development.. *Human molecular genetics*. PMID: 23773997
5. Investigating the impact of MCTP2 on immune suppression and drug resistance in glioblastoma.. *Functional & integrative genomics*. PMID: 41291342

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.2 |
| 高置信度残基 (pLDDT>90) 占比 | 16.3% |
| 置信残基 (pLDDT 70-90) 占比 | 45.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 29.5% |
| 有序区域 (pLDDT>70) 占比 | 61.9% |
| 可用 PDB 条目 | 2EP6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.2），有序残基占 61.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR013583; Pfam: PF00168, PF08372 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RGMA | 0.580 | 0.000 | — |
| FRMPD1 | 0.560 | 0.000 | — |
| OR6C75 | 0.511 | 0.000 | — |
| ANO4 | 0.499 | 0.000 | — |
| ZNF573 | 0.491 | 0.000 | — |
| AFF3 | 0.477 | 0.000 | — |
| TMEM182 | 0.472 | 0.000 | — |
| CPNE5 | 0.472 | 0.000 | — |
| NCALD | 0.462 | 0.000 | — |
| TMEM51 | 0.457 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| PRICKLE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.2 + PDB: 2EP6 | pLDDT=68.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MCTP2 — Multiple C2 and transmembrane domain-containing protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小878 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6DN12
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140563-MCTP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MCTP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6DN12
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6DN12-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
