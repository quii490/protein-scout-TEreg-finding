---
type: protein-evaluation
gene: "STAT4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STAT4 — REJECTED (研究热度过高 (PubMed strict=1042，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAT4 |
| 蛋白名称 | Signal transducer and activator of transcription 4 |
| 蛋白大小 | 748 aa / 85.9 kDa |
| UniProt ID | Q14765 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Flagellar centriole; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 748 aa / 85.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1042 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Flagellar centriole | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriole (GO:0005814)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1042 |
| PubMed broad count | 2127 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Precision medicine in systemic lupus erythematosus.. *Nature reviews. Rheumatology*. PMID: 37041269
2. STAT4 and STAT6, their role in cellular and humoral immunity and in diverse human diseases.. *International reviews of immunology*. PMID: 39188021
3. Variant STAT4 and Response to Ruxolitinib in an Autoinflammatory Syndrome.. *The New England journal of medicine*. PMID: 37256972
4. Histone demethylase KDM5D upregulation drives sex differences in colon cancer.. *Nature*. PMID: 37344599
5. Hyperglycemia-triggered lipid peroxidation destabilizes STAT4 and impairs anti-viral Th1 responses in type 2 diabetes.. *Cell metabolism*. PMID: 39488214

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 63.0% |
| 置信残基 (pLDDT 70-90) 占比 | 23.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 5.5% |
| 有序区域 (pLDDT>70) 占比 | 86.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.2，有序区 86.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR046991; Pfam: PF00017, PF01017, PF02864 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IL12RB2 | 0.996 | 0.541 | — |
| STAT1 | 0.994 | 0.535 | — |
| IL12RB1 | 0.990 | 0.091 | — |
| JAK1 | 0.988 | 0.285 | — |
| IFNG | 0.981 | 0.000 | — |
| JAK2 | 0.977 | 0.285 | — |
| IRF9 | 0.977 | 0.128 | — |
| STAT3 | 0.973 | 0.000 | — |
| TYK2 | 0.973 | 0.285 | — |
| JAK3 | 0.973 | 0.285 | — |

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
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 无 | pLDDT=86.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nuclear bodies; 额外: Flagellar centrio | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. STAT4 — Signal transducer and activator of transcription 4，研究基础较多，新颖性有限。
2. 蛋白大小748 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1042 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1042 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14765
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138378-STAT4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAT4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14765
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
