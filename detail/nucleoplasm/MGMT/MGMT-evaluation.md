---
type: protein-evaluation
gene: "MGMT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MGMT — REJECTED (研究热度过高 (PubMed strict=2894，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MGMT |
| 蛋白名称 | Methylated-DNA--protein-cysteine methyltransferase |
| 蛋白大小 | 207 aa / 21.6 kDa |
| UniProt ID | P16455 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 207 aa / 21.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2894 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=85.1; PDB: 1EH6, 1EH7, 1EH8, 1QNT, 1T38, 1T39, 1YFH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001497, IPR014048, IPR036217, IPR008332, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
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
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2894 |
| PubMed broad count | 6397 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. MGMT gene silencing and benefit from temozolomide in glioblastoma.. *The New England journal of medicine*. PMID: 15758010
2. Identifying active and inhibitor-resistant MGMT variants for gene therapy.. *American journal of human genetics*. PMID: 40398419
3. ATRX, OLIG2, MGMT, and IDH2 in Glioblastoma: Essential Molecular Mechanisms and Therapeutic Significance.. *Medicina (Kaunas, Lithuania)*. PMID: 40282990
4. MGMT in TMZ-based glioma therapy: Multifaceted insights and clinical trial perspectives.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 38242327
5. Correlation of MGMT promoter methylation status with gene and protein expression levels in glioblastoma.. *Clinics (Sao Paulo, Brazil)*. PMID: 22012047

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.1 |
| 高置信度残基 (pLDDT>90) 占比 | 72.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 13.5% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 1EH6, 1EH7, 1EH8, 1QNT, 1T38, 1T39, 1YFH, 8RGG, 8RGH, 8RTY |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1EH6, 1EH7, 1EH8, 1QNT, 1T38, 1T39, 1YFH, 8RGG, 8RGH, 8RTY）+ AlphaFold极高置信度预测（pLDDT=85.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001497, IPR014048, IPR036217, IPR008332, IPR036631; Pfam: PF01035, PF02870 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IDH1 | 0.934 | 0.000 | — |
| IDH2 | 0.893 | 0.000 | — |
| CDKN2A | 0.876 | 0.000 | — |
| RASSF1 | 0.868 | 0.000 | — |
| MLH1 | 0.866 | 0.088 | — |
| MPG | 0.849 | 0.000 | — |
| EGFR | 0.821 | 0.000 | — |
| PMS2 | 0.805 | 0.070 | — |
| OGG1 | 0.802 | 0.000 | — |
| MSH2 | 0.788 | 0.326 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| Q81U00 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| MGT1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.1 + PDB: 1EH6, 1EH7, 1EH8, 1QNT, 1T38,  | pLDDT=85.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. MGMT — Methylated-DNA--protein-cysteine methyltransferase，研究基础较多，新颖性有限。
2. 蛋白大小207 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2894 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2894 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16455
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170430-MGMT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MGMT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16455
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
