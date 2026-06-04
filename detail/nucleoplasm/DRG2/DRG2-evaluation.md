---
type: protein-evaluation
gene: "DRG2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DRG2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DRG2 |
| 蛋白名称 | Developmentally-regulated GTP-binding protein 2 |
| 蛋白大小 | 364 aa / 40.7 kDa |
| UniProt ID | P55039 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Cytosol; 额外: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 364 aa / 40.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012675, IPR045001, IPR031167, IPR006073, IPR031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Developmentally regulated GTP-binding protein-2 regulates adipocyte differentiation.. *Biochemical and biophysical research communications*. PMID: 34520979
2. PYRCR alleviates myocardial ischemia/reperfusion injury in mice via inhibiting DRG2-mediated cardiomyocyte pyroptosis.. *Acta pharmacologica Sinica*. PMID: 40588510
3. Developmentally regulated GTP-binding protein 2 levels in prostate cancer cell lines impact docetaxel-induced apoptosis.. *Investigative and clinical urology*. PMID: 34190439
4. DRG2 in macrophages is crucial for initial inflammatory response and protection against Listeria monocytogenes infection.. *Clinical immunology (Orlando, Fla.)*. PMID: 37918467
5. DRG2 is required for surface localization of PD-L1 and the efficacy of anti-PD-1 therapy.. *Cell death discovery*. PMID: 38802348

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.7 |
| 高置信度残基 (pLDDT>90) 占比 | 51.1% |
| 置信残基 (pLDDT 70-90) 占比 | 35.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 5.5% |
| 有序区域 (pLDDT>70) 占比 | 86.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=84.7，有序区 86.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012675, IPR045001, IPR031167, IPR006073, IPR031662; Pfam: PF01926, PF16897, PF02824 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RWDD1 | 0.999 | 0.993 | — |
| ZC3H15 | 0.968 | 0.795 | — |
| GCN1 | 0.964 | 0.904 | — |
| RWDD4 | 0.898 | 0.839 | — |
| RPL27A | 0.840 | 0.507 | — |
| DDX56 | 0.828 | 0.052 | — |
| RPS3 | 0.819 | 0.631 | — |
| RPS2 | 0.790 | 0.631 | — |
| RPS20 | 0.772 | 0.631 | — |
| RPL8 | 0.769 | 0.429 | — |

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
| 三维结构 | AlphaFold pLDDT=84.7 + PDB: 无 | pLDDT=84.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Vesicles, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DRG2 — Developmentally-regulated GTP-binding protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小364 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55039
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108591-DRG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DRG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55039
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
