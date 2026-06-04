---
type: protein-evaluation
gene: "RELA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RELA — REJECTED (研究热度过高 (PubMed strict=3926，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RELA / NFKB3 |
| 蛋白名称 | Transcription factor p65 |
| 蛋白大小 | 551 aa / 60.2 kDa |
| UniProt ID | Q04206 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 551 aa / 60.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3926 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.2; PDB: 1NFI, 2LSP, 2O61, 3GUT, 3QXY, 3RC0, 4KV1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013783, IPR014756, IPR002909, IPR033926, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- NF-kappaB complex (GO:0071159)
- NF-kappaB p50/p65 complex (GO:0035525)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3926 |
| PubMed broad count | 13322 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NFKB3 |

**关键文献**:
1. Blockade of LAG-3 and PD-1 leads to co-expression of cytotoxic and exhaustion gene modules in CD8(+) T cells to promote antitumor immunity.. *Cell*. PMID: 39121849
2. NIT2 dampens BRD1 phase separation and restrains oxidative phosphorylation to enhance chemosensitivity in gastric cancer.. *Science translational medicine*. PMID: 39565874
3. International real-world study of combination immunotherapy sequences in metastatic melanoma.. *Journal for immunotherapy of cancer*. PMID: 41314978
4. Unraveling Relatlimab-Specific Biology Using Biomarker Analyses in Patients with Advanced Melanoma in RELATIVITY-047.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 40607902
5. Mitogen- and stress-activated protein kinase (MSK1/2) regulated gene expression in normal and disease states.. *Biochemistry and cell biology = Biochimie et biologie cellulaire*. PMID: 36812480

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 46.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 34.3% |
| 有序区域 (pLDDT>70) 占比 | 55.0% |
| 可用 PDB 条目 | 1NFI, 2LSP, 2O61, 3GUT, 3QXY, 3RC0, 4KV1, 4KV4, 5U4K, 5URN |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1NFI, 2LSP, 2O61, 3GUT, 3QXY, 3RC0, 4KV1, 4KV4, 5U4K, 5URN）+ AlphaFold极高置信度预测（pLDDT=72.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013783, IPR014756, IPR002909, IPR033926, IPR000451; Pfam: PF16179, PF00554 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CREBBP | 0.999 | 0.991 | — |
| REL | 0.999 | 0.910 | — |
| NFKBIA | 0.999 | 0.999 | — |
| NFKBIE | 0.999 | 0.833 | — |
| NFKBIB | 0.999 | 0.948 | — |
| NFKB2 | 0.999 | 0.861 | — |
| EP300 | 0.999 | 0.950 | — |
| BRD4 | 0.999 | 0.974 | — |
| IKBKB | 0.999 | 0.877 | — |
| CHUK | 0.999 | 0.880 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000384273.3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:8246997 |
| EBI-289947 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| Nfkbib | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Nfkbia | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| - | psi-mi:"MI:0404"(comigration in non denaturing gel | pubmed:8246997 |
| NFKB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:8246997 |
| CHUK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:8246997 |
| PDCD11 | psi-mi:"MI:0096"(pull down) | pubmed:14624448 |
| MAP3K8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| REL | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 1NFI, 2LSP, 2O61, 3GUT, 3QXY,  | pLDDT=72.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol | 一致 |
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
1. RELA — Transcription factor p65，研究基础较多，新颖性有限。
2. 蛋白大小551 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3926 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3926 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q04206
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173039-RELA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RELA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q04206
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
