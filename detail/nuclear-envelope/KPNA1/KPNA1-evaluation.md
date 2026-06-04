---
type: protein-evaluation
gene: "KPNA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KPNA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KPNA1 / RCH2 |
| 蛋白名称 | Importin subunit alpha-5 |
| 蛋白大小 | 538 aa / 60.2 kDa |
| UniProt ID | P52294 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 538 aa / 60.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=57 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.2; PDB: 2JDQ, 3TJ3, 4B18, 6WX9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR032413, IPR000225, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- glutamatergic synapse (GO:0098978)
- NLS-dependent protein nuclear import complex (GO:0042564)
- nuclear pore (GO:0005643)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 57 |
| PubMed broad count | 128 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RCH2 |

**关键文献**:
1. Karyopherin Subunit Alpha 1 Enhances the Malignant Behaviors of Colon Cancer Cells via Promoting Nuclear Factor-κB p65 Nuclear Translocation.. *Digestive diseases and sciences*. PMID: 37038032
2. Gene-based genome-wide association studies and meta-analyses of conotruncal heart defects.. *PloS one*. PMID: 31314787
3. A Kpna1-deficient psychotropic drug-induced schizophrenia model mouse for studying gene-environment interactions.. *Scientific reports*. PMID: 38336912
4. Effects of Importin α1/KPNA1 deletion and adolescent social isolation stress on psychiatric disorder-associated behaviors in mice.. *PloS one*. PMID: 34767585
5. Enterovirus A71 2B Inhibits Interferon-Activated JAK/STAT Signaling by Inducing Caspase-3-Dependent Karyopherin-α1 Degradation.. *Frontiers in microbiology*. PMID: 34992585

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 75.7% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 11.7% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 2JDQ, 3TJ3, 4B18, 6WX9 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2JDQ, 3TJ3, 4B18, 6WX9）+ AlphaFold高质量预测（pLDDT=86.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR032413, IPR000225, IPR002652; Pfam: PF00514, PF16186, PF01749 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KPNB1 | 0.999 | 0.921 | — |
| STAT1 | 0.999 | 0.669 | — |
| CSE1L | 0.996 | 0.752 | — |
| NUP50 | 0.992 | 0.985 | — |
| KPNA4 | 0.963 | 0.091 | — |
| RELA | 0.950 | 0.409 | — |
| KPNA3 | 0.946 | 0.091 | — |
| NFKB1 | 0.923 | 0.105 | — |
| TERT | 0.913 | 0.905 | — |
| SOX2 | 0.906 | 0.903 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RELB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| aPKC | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| GCC88 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG3610 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Kap-alpha1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| kel | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Drep3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Doc3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| TAF9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| ANP32A | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 2JDQ, 3TJ3, 4B18, 6WX9 | pLDDT=86.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KPNA1 — Importin subunit alpha-5，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小538 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 57 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52294
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114030-KPNA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KPNA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52294
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
