---
type: protein-evaluation
gene: "CFAP119"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CFAP119 — REJECTED (数据不可用)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | CFAP119 |
| 数据状态 | 无 harvest packet |
| 评估日期 | 2026-06-03 |

### 2. 淘汰理由

**数据不可用**: 该基因在 harvest_packets 目录中无对应 JSON 文件，无法进行 /180 标准评分。可能原因包括：
- 该基因未被纳入原始 harvest pipeline
- UniProt 中无对应的人类蛋白条目
- 基因符号命名变化

### 3. 后续建议

- [ ] 确认基因符号是否为新命名（检查 HGNC 最新命名规范）
- [ ] 在 UniProt 检索对应的人类蛋白条目
- [ ] 如找到有效条目，重新运行 harvest pipeline 生成数据包

### 深度机制分析

CFAP119（纤毛与鞭毛相关蛋白119）在本次评估中因缺乏harvest数据包而无法完成标准/180评分——这意味着该基因在UniProt、HPA和STRING等核心数据库中缺少系统注释。尽管如此，基于基因名称中的"CFAP"前缀（Cilia and Flagella Associated Protein），合理推断CFAP119属于纤毛/鞭毛相关蛋白家族。该家族成员通常编码轴丝动力蛋白复合体亚基、放射辐或微管附属蛋白，定位于运动纤毛或精子鞭毛的"9+2"微管轴结构中。CFAP命名系统（CFAP20至CFAP300+）包含许多仅在纤毛蛋白质组学筛选中被鉴定、功能注释极不完整的孤儿蛋白——CFAP119的名称序号暗示其为该家族的中间成员。

CFAP前缀蛋白通常不含染色质调控结构域（即缺乏PHD指、bromodomain、chromodomain、AT-hook等经典DNA/组蛋白结合模块），其折叠倾向于微管结合重复（如WD40、TPR、Armadillo）或动力蛋白轻链/中间链的coiled-coil寡聚化域。然而，缺乏harvest数据包意味着无法检索AlphaFold pLDDT、UniProt域注释或STRING PPI——这些缺失从根本上阻止了任何可靠的机制推断。

从TE调控角度，CFAP家族的纤毛/鞭毛定位使其成为极不可能的候选者。TE沉默机制几乎完全限定于核区室（H3K9me3、DNA甲基化、piRNA途径）或邻近的核周区域，与轴丝动力学无关。仅在一种情境下CFAP蛋白可能与TE生物学产生间接联系——某些CFAP蛋白的突变导致精子鞭毛多发形态异常（MMAF）伴精子头部畸形，而精子头部畸形可能通过影响父本基因组递送间接影响受精卵中TE的表观遗传重编程。但这是极度间接且推测性的联系，无任何实验证据支持。

合计而言，CFAP119因数据缺失和纤毛特异定位的双重否定，其TE调控潜力评估为0。
- UniProt: https://www.uniprot.org/uniprotkb/?query=CFAP119
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CFAP119
