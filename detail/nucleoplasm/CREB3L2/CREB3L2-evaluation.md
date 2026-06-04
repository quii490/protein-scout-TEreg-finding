---
type: protein-evaluation
gene: "CREB3L2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CREB3L2 — REJECTED (研究热度过高 (PubMed strict=121，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CREB3L2 / BBF2H7 |
| 蛋白名称 | Cyclic AMP-responsive element-binding protein 3-like protein 2 |
| 蛋白大小 | 520 aa / 57.4 kDa |
| UniProt ID | Q70SY1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 520 aa / 57.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=121 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Endoplasmic reticulum | Supported |
| UniProt | Endoplasmic reticulum membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 121 |
| PubMed broad count | 165 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BBF2H7 |

**关键文献**:
1. Sclerosing Epithelioid Fibrosarcoma.. *Surgical pathology clinics*. PMID: 38278601
2. Aberrant phase separation drives membranous organelle remodeling and tumorigenesis.. *Molecular cell*. PMID: 40273917
3. Targeting CREB3L2-mediated lipid metabolism overcomes lenvatinib resistance and attenuates the progression of hepatocellular carcinoma.. *Cell death & disease*. PMID: 41285809
4. Sclerosing epithelioid fibrosarcoma.. *Wiener medizinische Wochenschrift (1946)*. PMID: 27631873
5. Comparative Analysis of CREB3 and CREB3L2 Protein Expression in HEK293 Cells.. *International journal of molecular sciences*. PMID: 33803345

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.5 |
| 高置信度残基 (pLDDT>90) 占比 | 13.5% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 20.2% |
| 低置信 (pLDDT<50) 占比 | 59.2% |
| 有序区域 (pLDDT>70) 占比 | 20.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.5），有序残基占 20.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CREB3 | 0.964 | 0.541 | — |
| CREB3L1 | 0.955 | 0.514 | — |
| CREB3L3 | 0.940 | 0.199 | — |
| CREB1 | 0.936 | 0.101 | — |
| ATF6B | 0.932 | 0.071 | — |
| ATF1 | 0.930 | 0.101 | — |
| ATF4 | 0.927 | 0.000 | — |
| CREB3L4 | 0.926 | 0.000 | — |
| EP300 | 0.922 | 0.073 | — |
| CREB5 | 0.922 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GCFC2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GAS7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GULP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CEP19 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PXN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RGS16 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ENSP00000329140.6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PTP4A1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| RND1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| ZNF212 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.5 + PDB: 无 | pLDDT=55.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus / Nucleoplasm, Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CREB3L2 — Cyclic AMP-responsive element-binding protein 3-like protein 2，研究基础较多，新颖性有限。
2. 蛋白大小520 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 121 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 121 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q70SY1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182158-CREB3L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CREB3L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q70SY1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
